# -*- coding:utf-8 -*-
# 此文件用于新建table
import psycopg2
import sys

av = sys.argv[1]
pg_connect = psycopg2.connect(
    database="example", user="example", password="example", host="example", port="5432")
sql = '''CREATE TABLE public.av{}(
    "time" integer,
    view integer,
    danmaku integer,
    reply integer,
    favorite integer,
    coin integer,
    share integer,
    "like" integer)
    WITH(OIDS = FALSE)'''.format(av)
pg_connect.cursor().execute(sql)
pg_connect.close()
print("table av{} 创建成功".format(av))