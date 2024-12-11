# 模拟卫星视角
software: Google Earth / KML
KML：专门用于描述地理信息的文件格式

`题目已知：`
We've captured data from a satellite that shows a flag located at the base of the Washington Monument.
The image was taken on March 26th, 2020, at 21:53:13（拍摄时间）
The satellite we used was:

REDACT(TLE 两行轨道根数)
1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995
2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337


Use a Google Earth Pro KML file to 'Link' to http://172.17.0.1:19021/cgi-bin/HSCKML.py
and 'LookAt' that spot from where the satellite when it took the photo and get us that flag!

`题目要求：在google earth中模拟卫星的拍摄角度、拍摄时间找flag`
### 启动
> socat -v tcp-listen:19020,reuseaddr exec:"docker run --rm -i -e SERVICE_HOST=172.17.0.1 -e SERVICE_PORT=19021 -e SEED=1000 -e FLAG=flag{test} -p 19021\:80 beckley\:challenge"

```text
test:
sudo make test
socat -v tcp-listen:19020,reuseaddr exec:"docker run --rm -i -e SERVICE_HOST=172.17.0.1 -e SERVICE_PORT=19021 -e SEED=1000 -e FLAG=flag{zulu49225delta\:GG1EnNVMK3-hPvlNKAdEJxcujvp9WK4rEchuEdlDp3yv_Wh_uvB5ehGq-fyRowvwkWpdAMTKbidqhK4JhFsaz1k} -p 19021\:80 beckley\:challenge" > log 2>&1 &
docker run -it --rm -e "HOST=172.17.0.1" -e "PORT=19020" beckley:solver
We've captured data from a satellite that shows a flag located at the base of the Washington Monument.
The image was taken on March 26th, 2020, at 21:53:13
The satellite we used was:
REDACT
1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995
2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337

Use a Google Earth Pro KML file to 'Link' to http://172.17.0.1:19021/cgi-bin/HSCKML.py
and 'LookAt' that spot from where the satellite when it took the photo and get us that flag!

Time is 21:53:13
curl http://172.17.0.1:19021/cgi-bin/HSCKML.py?CAMERA=-77.03,38.89,430000,40.3694166667,63.5358055556 -H 'User-Agent: GoogleEarth/7.3.2.5815(X11;Linux (5.2.0.0);en;kml:2.2;client:Pro;type:default)' -H 'Accept: application/vnd.google-earth.kml+xml, application/vnd.google-earth.kmz, image/*, */*' -H 'Accept-Language: en-US, *' -H 'Connection: keep-alive'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   343    0   343    0     0  11827      0 --:--:-- --:--:-- --:--:-- 11827
<description>flag{zulu49225delta:GG1EnNVMK3-hPvlNKAdEJxcujvp9WK4rEchuEdlDp3yv_Wh_uvB5ehGq-fyRowvwkWpdAMTKbidqhK4JhFsaz1k}</description>
flag{zulu49225delta:GG1EnNVMK3-hPvlNKAdEJxcujvp9WK4rEchuEdlDp3yv_Wh_uvB5ehGq-fyRowvwkWpdAMTKbidqhK4JhFsaz1k}

```


模拟google earth服务：

curl http://172.17.0.1:19021/cgi-bin/HSCKML.py?CAMERA=-77.03,38.89,430000,40.3694166667,63.5358055556 -H 'User-Agent: GoogleEarth/7.3.2.5815(X11;Linux (5.2.0.0);en;kml:2.2;client:Pro;type:default)' -H 'Accept: application/vnd.google-earth.kml+xml, application/vnd.google-earth.kmz, image/*, */*' -H 'Accept-Language: en-US, *' -H 'Connection: keep-alive'

CAMERA=[lookatLon],[lookatLat],[lookatRange],[lookatTilt],[lookatHeading]

背景知识：
卫星轨道描述6大参数（开普勒定律）、TLE数据、kml文件格式、视点构建方式、Skyfield天文库、SGP4轨道模型

![img.png](img/img.png)
