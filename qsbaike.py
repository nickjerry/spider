#coding=utf-8

import urllib2
import urllib
import re

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    article = re.compile(r'<div class="author.*?">.*?<h2>(.*?)</h2>.*?</div>\s*' + '<div class="content">(.*?)</div>' + '(.*?)</div>', re.S)
    text = re.findall(article, html)
    for item in text:
        hasimg = re.search('<img src', item[2])
        if not hasimg:
            print item[0], re.sub('\n{1,}', '\n', item[1]), '\n'
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print e.reason

