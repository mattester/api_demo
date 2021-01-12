import requests
url = "http://japi.juhe.cn/qqevaluate/qq"
param = {
    "key": "5639b2fd5ecdb46d8aa1d5f668afe5d3",
    "qq": "295424589"
}
r = requests.post(url=url,params=param)
print(r.json())