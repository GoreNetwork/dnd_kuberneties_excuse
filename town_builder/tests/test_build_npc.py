import requests
import json


def test_build_npc_endpoint():
    # Replace with the URL where your FastAPI app is running
    base_url = "http://localhost:7000"
    
    # Replace with the store_type you want to test

    # Define the endpoint URL
    endpoint_url = f"{base_url}/build_npc"

    try:
        # Make a POST request with the store_type parameter
        response = requests.post(endpoint_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Store built successfully.")
            print("Response JSON:", response.json())
        elif response.status_code == 404:
            print(f"Store type not found: {store_type}")
            print("Response JSON:", response.json())
        else:
            print(f"Request failed with status code {response.status_code}")
            print("Response JSON:", response.json())
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to test the endpoint
test_build_npc_endpoint()
