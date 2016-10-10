#!/usr/bin/env python
# coding:utf-8
# author:monster

"""
    将IP批量转为位置和坐标
"""

import GeoIP

ipip = open("/path/ip.txt")
geodb = "/path/GeoLiteCity.dat"
L = open("/path/L.txt", "a")

for ip in ipip:
    ip = ip.strip()
    gi = GeoIP.open(geodb, GeoIP.GEOIP_STANDARD)
    gir = gi.record_by_addr(ip)

    if gir is not None:
        LL = "{latlng:[" + str(gir['longitude']) + "," + \
            str(gir['latitude']) + "]},\n"
        print LL
        L.write(LL)

ipip.close()
L.close()
