# -*- coding:utf-8 -*-
# 此文件用于记录播放量增长
import requests
import psycopg2
import time
av = 00000000
sec = 300
pg_connect = psycopg2.connect(
    database="example", user="example", password="example", host="example", port="5432")
view = 0
while True:
    x = requests.get(
        'http://api.bilibili.com/archive_stat/stat?aid={}'.format(av), {"Host": "api.bilibili.com", "User-Agent": "AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36", "Accept-Encoding": "gzip, deflate"}).json()['data']
    if x['view'] > view:
        view = x['view']
        now_time = int(time.time())
        print(x, now_time)
        pg_connect.cursor().execute("INSERT INTO av{} VALUES({},{},{},{},{},{},{},{})".format(
            av, now_time, x['view'], x['danmaku'], x['reply'], x['favorite'], x['coin'], x['share'], x['like']))
        pg_connect.commit()
    else:
        print("av{}的播放量没有变化，等待{}秒再次获取信息".format(av, sec))
    time.sleep(sec)
pg_connect.close()
