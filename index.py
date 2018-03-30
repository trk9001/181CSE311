#! /usr/bin/env python

import cgitb
import pymysql

cgitb.enable()

print('Content-Type: text/html')
print('Location: /html/index.html')
print()

# conn = pymysql.connect(
#     db='cse311db',
#     user='trk',
#     passwd='',
#     host='localhost',
#     cursorclass=pymysql.cursors.DictCursor
# )
#
# with conn.cursor() as c:
#     c. execute('insert into test values (1, "One!")')
#     c. execute('insert into test values (2, "Two!")')
#     c. execute('insert into test values (3, "Three!")')
#
# conn.commit()
#
# with conn.cursor() as c:
#     c.execute('select * from test')
#     for r in c.fetchall():
#         print(r)
