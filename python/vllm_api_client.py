import requests
import json

base  = f'http://localhost:8000/'
api_key = "CELS"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def get_health():
    """
    Check the health status of the API server.    
    Returns: Response: HTTP response object from the health endpoint
    """
    response = requests.get(f"{base}/health", headers=headers)
    return response

def get_models():
    """
    Retrieve a list of available model names from the API.
    Returns: list: List of model root names
    """
    model_names = []
    response = requests.get(f"{base}/v1/models", headers=headers)
    for model in response.json()['data']:
        model_names.append(model['root'])
    return model_names

def get_version():
    """
    Get the current version of the API.
    Returns: str: Version number of the API
    """
    response = requests.get(f"{base}/version", headers=headers)
    return response.json()['version']

def test():
    """
    Test function to demonstrate the usage of all API endpoints.
    Prints the health status, available models, and API version.
    """
    print(f'health: {get_health()}')
    print(f'models: {get_models()}')
    print(f'version: {get_version()}')

if __name__ == '__main__':
    test()
