import requests

class BuildReqRes:

    def __init__(self):
        print("Initializing Requests and Response from Cloud")

    def get_api_url(self,date):
        api_url = "https://api.github.com/repos/apache/spark/commits?since=" + date + "T00:00:00Z&until=" + date + "T00:00:00"
        print("API URL Creation Successful")
        return api_url

    def get_response(self,api_url):
        response = requests.get(api_url)
        return response if response.ok else response.raise_for_status()