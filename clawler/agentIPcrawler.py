#!/usr/bin/env python
# coding:utf-8
# author:Monster

"""
    本程序的主要作用是爬取xici代理的ip端口信息
"""

import re
import time
import urllib2

#要爬取的页数
n = int(raw_input("请输入要爬取的页数: "))

#加入header头模仿浏览器
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

#URL接口
#国内高匿
url = "http://www.xicidaili.com/nn/"
#国内透明
#url = "http://www.xicidaili.com/nt/"
#国外高匿
#url = "http://www.xicidaili.com/wn/"
#国外透明
#url = "http://www.xicidaili.com/wt/"

#获取单个网页的内容
def get_content(url):
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req)
    content = response.read()
    response.close()

    return content

#获取单个网页的ip信息
def get_ip(url):
    c = get_content(url)
    reg = r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\s*<td>(\d*)</td>'
    p = re.compile(reg)
    ips = re.findall(p,c)

    return ips

#将输出的结果保存为文件，并以时间为文件名保存
def file_output(ips):
    t_time = time.strftime("%Y-%m-%d",time.localtime())
    result = "result_"+t_time+".txt"
    file = open(result,"a")
    file.write(ips)
    file.close()

def main():
    print "[+] 开始爬取..."
    for i in range(n):
        urls = url+str(i+1)
        print "[+] "+urls
        ips = get_ip(url)
        for k,v in ips:
            result = k+":"+v+"\n"
            file_output(result)
    print "[+] 爬取结束"

if __name__=="__main__":
    main()
