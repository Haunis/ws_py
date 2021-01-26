import requests

print(requests.__file__)#/usr/lib/python3/dist-packages/requests/__init__.py

response = requests.get("https://www.baidu.com")

print(response.status_code)
print(response.text)