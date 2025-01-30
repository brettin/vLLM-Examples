import requests
import json

base  = f'http://localhost:8000/'
api_key = "CELS"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

default_data = {"api-key": api_key}

def get_openapi_json():
    response = requests.get(f"{base}/openapi.json", headers=headers)
    return response.json()

def get_docs():
    response = requests.get(f"{base}/docs", headers=headers)
    return response.text

def get_oauth2_redirect():
    response = requests.get(f"{base}/docs/oauth2-redirect", headers=headers)
    return response.text

def get_redoc():
    response = requests.get(f"{base}/redoc", headers=headers)
    return response.text

def get_health():
    response = requests.get(f"{base}/health", headers=headers)
    return response

def get_models():
    model_names = []
    response = requests.get(f"{base}/v1/models", headers=headers)
    for model in response.json()['data']:
        model_names.append(model['root'])
    return model_names

def get_version():
    response = requests.get(f"{base}/version", headers=headers)
    return response.json()['version']

# TODO: The data structure for the post methods needs to be figured out.
def post_tokenize():
    response = requests.post(f"{base}/tokenize", headers=headers, params=default_data, json={"input": input})
    return response.json()

def post_detokenize():
    response = requests.post(f"{base}/detokenize", headers=headers, params=default_data)
    return response.json()

def post_chat_completions():
    response = requests.post(f"{base}/v1/chat/completions", headers=headers, params=default_data)
    return response.json()

def post_completions():
    response = requests.post(f"{base}/v1/completions", headers=headers, params=default_data)
    return response.json()

def post_embeddings():
    response = requests.post(f"{base}/v1/embeddings", headers=headers, params=default_data)
    return response.json()

def post_pooling():
    response = requests.post(f"{base}/pooling", headers=headers, params=default_data)
    return response.json()

def post_score():
    response = requests.post(f"{base}/score", headers=headers, params=default_data)
    return response.json()

def post_v1_score():
    response = requests.post(f"{base}/v1/score", headers=headers, params=default_data)
    return response.json()


def test():

    
    print(f'health: {get_health()}')
    print(f'models: {get_models()}')
    print(f'version: {get_version()}')
    
    #print(f'openapi.json: {json.dumps(get_openapi_json(), indent=2)}')
    #print(f'docs: {json.dumps(get_docs(), indent=2)}')
    #print(f'oauth2-redirect: {json.dumps(get_oauth2_redirect(), indent=2)}')
    #print(f'redoc: {json.dumps(get_redoc(), indent=2)}')

    #print(f'tokenize: {json.dumps(post_tokenize(input="Hello, world!"), indent=2)}')
    #print(f'detokenize: {json.dumps(post_detokenize(), indent=2)}')
    #print(f'chat/completions: {json.dumps(post_chat_completions(), indent=2)}')
    #print(f'completions: {json.dumps(post_completions(), indent=2)}')
    #print(f'embeddings: {json.dumps(post_embeddings(), indent=2)}')
    #print(f'pooling: {json.dumps(post_pooling(), indent=2)}')
    #print(f'score: {json.dumps(post_score(), indent=2)}')
    #print(f'v1/score: {json.dumps(post_v1_score(), indent=2)}')


if __name__ == '__main__':
    test()
