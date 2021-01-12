import requests
#url地址
url = "http://japi.juhe.cn/qqevaluate/qq"
#请求参数
param = {
    "key":"5639b2fd5ecdb46d8aa1d5f668afe5d3",
    "qq":"295424589"
}
r = requests.get(url=url,params=param)
print(r.text)
print(r.json()) #json解释器
reason = r.json()['result']['data']['conclusion']
print(reason)
