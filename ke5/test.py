import requests
url = "http://japi.juhe.cn/qqevaluate/qq"
parm={
    "key":"5639b2fd5ecdb46d8aa1d5f668afe5d3",
    "qq":"123456789"
}
r = requests.get(url=url,params=parm)
print(r.text)