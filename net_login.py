# -*- coding:utf-8 -*-
import getopt
import json
import urllib
import urllib2

import sys


def net_login(username, password):
    url = 'http://p.nju.edu.cn/portal_io/login'
    data = {'username': username, 'password': password}
    post_data = urllib.urlencode(data).encode('utf-8')
    try:
        request = urllib2.Request(url, post_data)
        response = urllib2.urlopen(request)
        # 从结果内容中查找是否有特定字符串
        res = json.loads(response.read().decode('utf-8'))
        print res["reply_code"]
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


def main(argv):
    ttype = ''
    user = ''
    pwd = ''
    try:
        opts, args = getopt.getopt(argv, "t:u:p:")
    except getopt.GetoptError:
        print 'net_login.py -t <type> -u <username> -p <password>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-t':
            ttype = arg
        elif opt == '-u':
            user = arg
        elif opt == '-p':
            pwd = arg

    if ttype == '0':
        net_login(username=user, password=pwd)
    else:
        net_logout()


if __name__ == '__main__':
    main(sys.argv[1:])
