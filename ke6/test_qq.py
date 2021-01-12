import pytest
import requests
def test_1():
    """QQ号码—必填项key，输入正确地key，请求成功"""
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm={
        "key":"5639b2fd5ecdb46d8aa1d5f668afe5d3",
        "qq":"123456789"
    }
    r = requests.get(url=url,params=parm)
    print(r.text)
    #实际结果
    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    #预期结果
    expect_result = { "error_code": 0}

    #断言
    assert error_code == expect_result["error_code"]

def test_2():
    """qq-必填项key不传"""
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm={
        "key":"",
        "qq":"123456789"
    }
    r = requests.get(url=url,params=parm)
    print(r.text)
    #实际结果
    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    #预期结果
    expect_result = { "error_code": 10001}

ZV
    #断言
    assert error_code == expect_result["error_code"]

def test_3_1():


    """	key传数字"""
    url = "http://japi.juhe.cn/qqevaluate/qq"
    parm={
        "key":"12345678",
        "qq":"295424589"
    }
    r = requests.get(url=url,params=parm)
    print(r.text)
    #实际结果
    error_code = r.json()["error_code"]
    print("取到的error_code：%s"%error_code)
    #预期结果
    expect_result = { "error_code": 10001}
    #断言
    assert error_code == expect_result["error_code"]