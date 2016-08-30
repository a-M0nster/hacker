#!/usr/bin/env python
#coding:utf-8

import random

random_number = random.randint(1,100)
count = 0

print "猜数游戏"
print "******************************"

while True:
    number_str = raw_input("[+] 请输入猜测的数字: ")
    count += 1

    if not number_str.isdigit():
        print "[!] 请输入数字"
    elif not 0<=int(number_str)<=100:
        print "[!] 范围为0-100"
    else:
        number_int = int(number_str)

        if number_int == random_number:
            print "[#] 回答正确 正确的数字为 %s 当前尝试的次数为 %s" % (number_str,count)
            break
        elif number_int > random_number:
            print "n[#] 输入大了 当前尝试的次数为 %s" % count
        elif number_int < random_number:
            print "[#] 输入小了 当前尝试的次数为 %s" % count
        else:
            print "程序出问题 不能工作了"

print "******************************"