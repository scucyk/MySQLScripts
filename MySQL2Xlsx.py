#!/usr/bin/env python
# coding:utf-8

import sys
import MySQLdb
import xlsxwriter

# 将默认的编码改成utf-8
reload(sys)
sys.setdefaultencoding('utf-8')


# 导出数据到xlsx文件

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='dba_admin', passwd='12345678', db='db_monitor')
cur = conn.cursor()

statement = 'select id, name, address from test_tb1'

cur.execute('set names utf8')
cur.execute(statement)
result = cur.fetchall()

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 40)
worksheet.set_column('B:B', 40)
worksheet.set_column('C:C', 40)


worksheet.write_string(0, 0, 'ID')
worksheet.write_string(0, 1, '姓名')
worksheet.write_string(0, 2, '地址')

for i in xrange(len(result)):
        try:
                worksheet.write(i+1, 0, result[i][0])
                worksheet.write(i+1, 1, result[i][1])
                worksheet.write(i+1, 2, result[i][2])
        except Exception, e:
                print i, 'line has problem'

workbook.close()

cur.close()
conn.close()

