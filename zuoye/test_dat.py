import requests
def day(key,date,url=None):
    url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
    parm = {
        "key": key,
        "date": date
    }
    r = requests.get(url=url, params=parm)
    error_code = r.json()["error_code"]
    return error_code
def test_11():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce",date="1/1")
    assert error_code == 0
def test_12():
    error_code = day(key="",date="1/1")
    assert error_code == 10001
def test_13():
    error_code = day(key="null", date="1/1")
    assert error_code == 10001
def test_14():
    error_code = day(key="", date="1/1")
    assert error_code == 10001
def test_15_1():
    error_code = day(key="asdfghj", date="1/1")
    assert error_code == 10001
def test_15_1():
    error_code = day(key="asdfghj", date="1/1")
    assert error_code == 10001
def test_15_2():
    error_code = day(key="1234567788", date="1/1")
    assert error_code == 10001
def test_15_4():
    error_code = day(key="￥……%……&￥￥", date="1/1")
    assert error_code == 10001
def test_16():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="1/1")
    assert error_code == 0
def test_17():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="null")
    assert error_code == 206300
def test_18():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="")
    assert error_code == 206300
def test_19_1():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="12345")
    assert error_code == 206300
def test_19_2():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="aafdd")
    assert error_code == 206300
def test_19_3():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="///////")
    assert error_code == 206300
def test_19_4():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="？*&……")
    assert error_code == 206300
def test_20():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="-1/1")
    assert error_code == 206300
def test_21():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="0/1")
    assert error_code == 206300
def test_22():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="null")
    assert error_code == 206300
def test_23():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="13/2")
    assert error_code == 206300
def test_24_1():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="a/1")
    assert error_code == 206300
def test_24_2():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="2/13")
    assert error_code == 0
def test_24_3():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="/2/20")
    assert error_code == 206300
def test_24_4():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="&/24")
    assert error_code == 206300
def test_25():
    error_code = day(key="4a036628c36055d1e04c42fa5ebde1ce", date="1/-1")
    assert error_code == 206300
