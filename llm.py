from ollama import chat
from ollama import ChatResponse
from ollama import Client

prompt=input("Enter your Prompt: ")

client = Client(
  host='http://localhost:11434',
  headers={'x-some-header': 'some-value'}
)
stream = client.chat(model='deepseek-r1', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
], stream=True)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
