
# 招聘爬虫
import re
import urllib

url="http://jyzx.zuel.edu.cn/career/preachmore"
comments=[]#存储所有评论的列表
#以爬取评论前30页为例
for i in range(1,31):
    #设定get的值
    mydata=urllib.parse.urlencode({
        'overdue': 2,
        'title': '',
        'sponsor':'',
        'time':'',
        'field.fieldname':'',
        'pageNo': i
    }).encode("utf-8")
    #发送POST请求进行爬取
    req=urllib.request.Request(url,mydata)
    print(req)
    commentdata=urllib.request.urlopen(req).read().decode("utf-8","ignore")
    comment = re.findall('<tr>(.*?)</tr>',commentdata,re.S)#使 . 匹配包括换行在内的所有字符
    print(comment)