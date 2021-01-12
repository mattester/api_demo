import requests
def day(key,date,url=None):
    url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
    parm = {
        "key": key,
        "date": date
    }
    r = requests.get(url=url, params=parm)
    error_code = r.json()["error_code"]
    print(r.json())

day(key="",date="1/1")
