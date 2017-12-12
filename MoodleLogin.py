# -*- coding:utf-8 -*-

import urllib
import urllib2


def moodle_login():
    url = 'http://218.94.159.99/login/index.php'
    username = 'xxxxxx'  # 可将密码等保存至文件
    password = 'xxxxxxx'
    data = {'username': username, 'password': password}
    postdata = urllib.urlencode(data).encode('utf-8')
    try:
        request = urllib2.Request(url, postdata)
        response = urllib2.urlopen(request)
        # 从结果内容中查找是否有特定字符串
        res = response.read().decode('utf-8')
        print res
        # print res["reply_code"]
    except Exception as e:
        print(e)


if __name__ == '__main__':
    moodle_login()
