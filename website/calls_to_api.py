import requests

url = "http://localhost:8000"

def pull_new_town():
    endpoint_url = f"{url}/build_town"
    response = requests.post(endpoint_url, json={"store_type": "combat_store"})
    return response.json()
pull_new_town()

