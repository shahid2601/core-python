# import a module to handle GitHub API requests
import requests

# Create a dictionary to store GitHub API credentials
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

data = response.json()

for i in range(len(data)):
    print(data[i]["user"]["login"])