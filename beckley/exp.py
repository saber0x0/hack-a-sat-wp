#!/usr/bin/python3
# coding:utf-8
# Mans00r
import os
import re

from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import Topos
import pwnlib.tubes


# 查询某一时刻卫星在地心天球参考系中XYZ坐标
ts = load.timescale()
line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'

satellite = EarthSatellite(line1, line2, 'ISS(ZARYA)', ts)
# print(satellite)

t = ts.utc(2024, 12, 9, 22, 27, 30)
geocentric = satellite.at(t)
# print(geocentric.position.km)
# result:
# ISS(ZARYA) catalog #13337 epoch 2020-03-27 09:07:58 UTC
# [-6735.95440499   788.5784274    478.63402509]

# 查询某一时刻，地面观察者视角相对卫星位置
"""
bluffton = Topos('38.8894939 N', '77.0352791 W')
difference = satellite - bluffton
topocentric = difference.at(t)
alt, az, distance = topocentric.altaz()
# print(alt, az, distance)
# result：
# -66deg 42' 20.0"(地平高度)（Altitude）
# 339deg 07' 58.8"(方位角)（Azimuth）
# 8.14203e-05 au(天文距离)（Astronomical Unit）
"""


# exp
ts = load.timescale()
line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'
# EarthSatellite SGP4简化模式模型，，at方法生成天空位置，可以与其他向量加减，ts是时间刻度，用于生成epoch值（最准确的时间点）。
satellite = EarthSatellite(line1, line2, 'REDACT', ts)
t = ts.utc(2020, 3, 26, 21, 53, 13)
photo = Topos('38.8894838 N','77.0352791 W')
difference = satellite - photo
topocentric = difference.at(t)
alt, az, distance = topocentric.altaz()
print('Altitude(deg):%f' % alt.degrees)
print('Azimuth(def): %f' % az.degrees)
print('Range(m):%d' % int(distance.m))
tilt = 90 -alt.degrees
print('Tilt(deg): %f' % tilt)
heading = (180 + az.degrees) % 360
print('Heading(deg): %f' % heading)
# >>更新remote.kml
ipaddr = "172.17.0.1"
ipport = "19021"
url = ipaddr + ":" + ipport
cmd = ('curl http://' + url + '/cgi-bin/HSCKML.py?CAMERA=' + str("77.0352791") + ',' + str("38.8894838") + ','
       + str(int(distance.m)) + ',' + str(tilt) + ',' + str(heading) +
       ' -H \'User-Agent: GoogleEarth/7.3.2.5815(X11;Linux (5.2.0.0);en;kml:2.2;client:Pro;type:default)\' -H \'Accept: application/vnd.google-earth.kml+xml, application/vnd.google-earth.kmz, image/*, */*\' -H \'Accept-Language: en-US, *\' -H \'Connection: keep-alive\'')
print(cmd)

result = os.popen(cmd).readlines()

# Grep for flag{} in Curl output
for line in result:
    m = re.search("flag{.*}", line)
    if m:
        print(line.strip())
        print(m.group(0))
