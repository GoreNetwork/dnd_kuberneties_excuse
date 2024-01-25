import requests
import json
from pprint import pprint


def test_build_store_endpoint():
    # Replace with the URL where your FastAPI app is running
    base_url = "http://localhost:8000"
    
    # Define the endpoint URL
    endpoint_url = f"{base_url}/build_town"

    try:
        # Make a POST request with the store_type parameter
        response = requests.post(endpoint_url)
        return response.json()
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to test the endpoint
pprint (test_build_store_endpoint())
