import requests

url = "http://dnd_kuberneties_excuse-dnd_api-1:8000"

def pull_new_town():
    endpoint_url = f"{url}/build_town"
    response = requests.post(endpoint_url, json={"store_type": "combat_store"})
    return response.json()


