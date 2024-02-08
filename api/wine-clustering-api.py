import csv
import pandas as pd
import requests

from flask import Flask, jsonify
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Download and load dataset
def load_dataset(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as file:
            file.write(response.content)
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"Error downloading file: {err}")

# Save the dataset via API, load it into Kmeans and map the labels of cultivars
def process_data():
    filename = "wine-clustering.csv"
    output_filename = "wine-clustering-labeled.csv"
    
    try:
        load_dataset("https://storage.googleapis.com/the_public_bucket/wine-clustering.csv", filename)
        df = pd.read_csv(filename)
        
        numeric_data = df.select_dtypes(include=['float64', 'int64'])
        scaled_data = StandardScaler().fit_transform(numeric_data)
        
        kmeans = KMeans(n_clusters=3, algorithm='elkan')
        kmeans.fit(scaled_data)
        cluster_labels = kmeans.labels_
        
        df['Cultivars'] = cluster_labels
        df['Cultivars'] = df['Cultivars'].map({0: 1, 1: 2, 2: 3})
        
        df.to_csv(output_filename, index=False)
    except Exception as e:
        raise RuntimeError(f"Error processing data: {e}")

# Read the CSV file and return the data as JSON
def get_json_data(filename):
    try:
        with open(filename, 'r') as file:
            csv_data = list(csv.DictReader(file))
        return jsonify(csv_data)
    except Exception as e:
        raise RuntimeError(f"Error reading CSV: {e}")

@app.route('/api', methods=['GET'])
def get_clustered_data():
    try:
        process_data()
        return get_json_data("wine-clustering-labeled.csv")
    except RuntimeError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
