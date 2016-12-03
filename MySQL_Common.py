#!/usr/bin/env python
# coding:utf-8

import MySQLdb


conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='dba_admin', passwd='12345678', db='db_monitor')
cur = conn.cursor()

statement = 'select id, name, address from test_tb1'

cur.execute('set names utf8')
cur.execute(statement)
result = cur.fetchall()

for i in xrange(len(result)):
        try:
                print result[i][0], result[i][1], result[i][2]
        except Exception, msg:
                print msg

cur.close()
conn.close()
