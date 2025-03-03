from ollama import chat
from ollama import ChatResponse
from ollama import Client

prompt=input("Enter your Prompt: ")

client = Client(
  host='http://localhost:11434',
)
stream = client.chat(model='gemma2:2b', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
], stream=True)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
