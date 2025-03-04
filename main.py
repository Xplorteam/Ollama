import ollama

client = ollama.Client()

model = 'llama3.2'
prompt = 'Hello, bro'

response = client.generate(model, prompt)

print(f'Generated response: {response.response}')