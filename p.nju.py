#coding=utf-8

import urllib2
import urllib
import re

def parse_args():
    import getopt, sys
    opts, args = getopt.getopt(sys.argv[1:], "u:p:", ['user=', 'password='])
    global name, passwd
    for opt,arg in opts:
        if opt in ('-u', '--user'):
            name = arg
        elif opt in ('-p', '--password'):
            passwd = arg
    if passwd == '':
        sys.stderr.write('password not specified!\n')
        exit(0)

try:
    username = '141242068'
    passwd = '**************'
    parse_args()
    login = 'http://p.nju.edu.cn/portal_io/login'
    data = {'username':username, 'password':passwd}
    data = urllib.urlencode(data)
    request = urllib2.Request(login, data)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError as e:
    if hasattr(e, 'reason'):
        print e.reason
