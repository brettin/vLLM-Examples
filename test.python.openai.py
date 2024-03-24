from openai import OpenAI

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000,
                    help="display a square of a given number")

args = parser.parse_args()
print(f'using port: {args.port}')

# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = f"http://localhost:{args.port}/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

# sampling_params = SamplingParams({"prompt_logprobs": 1, "logprobs": 1))
chat_response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    # logprobs=1,
    # top_logprobs=1,
    messages=[
        {"role": "user", "content": "A detailed description of the biochemical \
            function 5-(hydroxymethyl)furfural/furfural transporter is"},
    ],
    temperature=0.0,
    max_tokens=2056,
)
print("Chat response:", chat_response)
