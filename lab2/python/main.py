import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("Статус:", response.status_code)
print("Відповідь:")
print(response.text)
