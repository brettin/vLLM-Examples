from openai import OpenAI

# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

chat_response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    messages=[
        {"role": "user", "content": "A detailed description of the biochemical \
            function 5-(hydroxymethyl)furfural/furfural transporter is"},
    ],
    temperature=0.0,
    max_tokens=2056,
)
print("Chat response:", chat_response)
