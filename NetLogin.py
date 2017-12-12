# -*- coding:utf-8 -*-

import json
import urllib
import urllib2


def net_login():
    url = 'http://p.nju.edu.cn/portal_io/login'
    username = '151250xxx'  # 可将密码等保存至文件
    password = 'xxxxxx'
    data = {'username': username, 'password': password}
    postdata = urllib.urlencode(data).encode('utf-8')
    try:
        request = urllib2.Request(url, postdata)
        response = urllib2.urlopen(request)
        # 从结果内容中查找是否有特定字符串
        res = json.loads(response.read().decode('utf-8'))
        # print res["reply_code"]
    except Exception as e:
        print(e)


def net_logout():
    url = 'http://p.nju.edu.cn/portal_io/logout'
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        # 从结果内容中查找是否有特定字符串
        res = response.read().decode('utf-8')
        print res
    except Exception as e:
        print(e)


if __name__ == '__main__':
    net_login()
