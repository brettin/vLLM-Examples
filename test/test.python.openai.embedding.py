from openai import OpenAI

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000,
                    help="port number, default 8000")
parser.add_argument("--host", type=str, default="localhost",
            help="host name, default localhost")
parser.add_argument("--model", type=str, default="mistralai/Mixtral-8x7B-Instruct-v0.1",
                    help="repo/model, default mistralai/Mixtral-8x7B-Instruct-v0.1")
parser.add_argument("--key", type=str, default="EMPTY",
        help="the key passed to the vllm entrypoint when it was started")

args = parser.parse_args()
print(f'using host: {args.host}')
print(f'using port: {args.port}')
print(f'using api-key: {args.key}')

# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_base = f"http://{args.host}:{args.port}/v1"


client = OpenAI(
    api_key=args.key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id
print(f'Using model: {model}')

responses = client.embeddings.create(
    input=[
        "Hello my name is",
        "The best thing about vLLM is that it supports many different models"
    ],
    model=model,
    encoding_format="float",
)
print(f'{responses}')

if responses.data is not None:
    print(f'{responses.data}')
    for data in responses.data:
        print(data.embedding)  # list of float of len 4096
else:
    print("response.data is None")

