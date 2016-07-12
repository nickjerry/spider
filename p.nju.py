#coding=utf-8

import urllib2
import urllib
import re

try:
    username = '141242068'
    passwd = '**************'
    login = 'http://p.nju.edu.cn/portal_io/login'
    data = {'username':username, 'password':passwd}
    data = urllib.urlencode(data)
    request = urllib2.Request(login, data)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print e.reason
