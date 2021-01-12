import requests
url = "https://www.cnblogs.com/"
r = requests.get(url=url,verify=False)
print(r.text)
