# Data Analysis and Wine Clustering

This project focuses on the analysis of a dataset containing the results of a chemical analysis of wines produced in a specific region of Italy, but derived from three different grape varieties. The main objective is to explore the relationships and patterns between the various chemical properties of the wines and to group them according to these properties using clustering techniques, Data Science practices, development, containerization and deployment of a proprietary API.

---

## About the branches of the Repository:

This project managed not only to perform Clustering techniques, Data Science, development, dockerization and deployment of an ([API](https://dcajiao-wine-clustering-api.onrender.com/)) to perform queries on the dataset resulting from clustering, it also managed to deploy a ([Web Page](https://dcajiao-wine-clustering.onrender.com/)) to display the results using *creative ideas and storytelling.*

To accomplish this, I made use of [Render.com](http://render.com/)'s free service. This service connects directly with this Github repository to make specific deployments by Branches and/or Commits, so, being a free service, it was not possible to deploy everything in the same direction since the free service has certain processing limitations, so each Branch of this repository (API and webpage) had to be deployed as a separate service each. However, this is just a technical detail, since everything works correctly and is mentioned to be taken into account when reviewing this code.

---

## **Data Analysis:**

In the process of Data Analysis, it was possible to extract the dataset by consulting the API, and after that, a process of EDA, Visualizations and with this to go to the Grouping Analysis…

More details on the phases:

### **Libraries**

Various Python libraries, including pandas, matplotlib, seaborn and scikit-learn, are used for data analysis and visualization.

### **Data Import Using API**

The data is downloaded from a URL using the `requests` library and saved in a CSV file locally for further processing.

### **Initial Exploration of the Dataset**

An initial exploration of the data set is performed to understand its structure, dimensions and distribution of values.

### **Data Visualization**

Visualizations, such as heat maps and bar charts, are generated to explore the correlations between the different chemical properties of the wines and to identify visual patterns.

For example, using a correlation matrix, we are able to identify which variables are related to each other for all wines.

![https://github.com/DCajiao/Wine-Clustering-Challenge/blob/main/graphics/corr/Correlations_between_Wine_data_features.png?raw=true](https://github.com/DCajiao/Wine-Clustering-Challenge/blob/main/graphics/corr/Correlations_between_Wine_data_features.png?raw=true)

---

## **Cluster Analysis**

In the clustering analysis process, the scikit-learn library and the elbow method took center stage.

### **How Many Clusters Should Be Used?**

For this purpose, the elbow method was applied to determine the optimal number of clusters for wine clustering.

![https://raw.githubusercontent.com/DCajiao/Wine-Clustering-Challenge/main/graphics/elbowmethod/elbowmethod.png](https://raw.githubusercontent.com/DCajiao/Wine-Clustering-Challenge/main/graphics/elbowmethod/elbowmethod.png)

The result of this process tells us that the optimal number of clusters is at 3. This is evident in the graph, where we can see that this point represents the inflection point, suggesting a natural division of the data into three distinct groups. Moreover, according to the context of the dataset, the wines come from 3 different areas of Italy, which coincides with the conclusions of the elbow method. This is why, in this case, clustering was performed with 3 clusters, which represent each crop, respectively.

---

### **KMeans Model**

The KMeans algorithm is applied to group the wines into clusters based on their chemical properties. PCA is used to reduce the dimensionality and visualize the clusters in a two-dimensional graph.

![https://github.com/DCajiao/Wine-Clustering-Challenge/blob/main/graphics/clustering/Clustering.png?raw=true](https://github.com/DCajiao/Wine-Clustering-Challenge/blob/main/graphics/clustering/Clustering.png?raw=true)

---

### **Questions of Value for the Analysis of Results**

Key questions related to the chemical properties of the wines are formulated and the results are analyzed to ground the analysis.

1. What are the ten correlations with the highest percentage among wine attributes?
2. How many wines do we have for each crop?
3. How correlated are the wine characteristics of each crop?
4. In which crop is the most intensely colored wine produced?
5. In which crop is the wine with the greatest sensation of freshness produced?
6. In which crop is the healthiest wine produced?
7. What can we say about each crop?
8. How does the chemical profile of wines produced in different geographic regions vary?

Note: Find the answers to these questions at [https://dcajiao-wine-clustering.onrender.com](https://dcajiao-wine-clustering.onrender.com/).

---

### **Data Exporting (Output)**

The processed and labeled DataFrame after clustering, including the labels of each crop assigned to each wine, is saved in a CSV file for later use.

---