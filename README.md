# *API Wine Clustering*
![API Wine Clustering](https://github.com/DCajiao/Wine-Clustering-Challenge/blob/webpage/images/api.png?raw=true)
## Configuring and Running the Docker Container.

To configure and run the Docker container containing our wine data analytics API, follow these steps:

1. Clone or download the Github repository on your local machine.
2. Make sure you have Docker installed on your system.
3. Open the **`docker-compose.yml`** file and make sure the path to the **`build`** folder is correct.
4. Run the following command in your terminal to build and run the Docker container:

```Docker
  docker-compose up --build
```
5. The API will now be up and running and accessible at http://localhost:5000.


## Accessing the Data through the API: Usage/Examples

Once the API is up and running on your local machine, you can access the data using HTTP requests. Here is an example of how to do this using Python and the  **`requests`** library:

```Python
import requests

url = '<http://localhost:5000/>'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error getting data from API.")
}
```
Or if you want to make the request to the already deployed API, you can also specify its URL: 
[API Wine Clustering](https://dcajiao-wine-clustering-api.onrender.com)
```Python
import requests

url = 'dcajiao-wine-clustering-api.onrender.com'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error getting data from API.")
}
```
## Dockerization of the API:

The API is packaged inside a container using a Dockerfile, where critical dependencies are specified and instructions for building the container image are provided. In parallel, the docker-compose.yml file defines the configuration required to build and run the Docker container, ensuring a consistent and efficient development and deployment environment.

## About deployment and response times
At the moment the API is deployed on a free Render service, it doesn't provide us with a lot of processing power, only what is  necessary for the API to work properly. So sometimes it may take a few seconds before delivering a response, I ask you to be patient. 

## Check out

 - [API Wine Clustering](https://dcajiao-wine-clustering-api.onrender.com)
 - [Wine Clustering Challenge Webpage](https://dcajiao-wine-clustering.onrender.com)

