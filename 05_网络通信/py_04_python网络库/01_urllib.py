import urllib.request

print(urllib.request.__file__) #/usr/lib/python3.5/urllib/request.py

req = urllib.request.urlopen("https://www.baidu.com")
content = req.read()
print(content)

