#! /var/www/trk/venv/bin/python

import cgi
import cgitb
import html
import passlib
import pymysql

cgitb.enable()

print('Content-Type: text/html')
print()

form = cgi.FieldStorage()

if len(form) < 10:
    print('len', len(form))

if form.getvalue('from') == form.getvalue('to'):
    print('Zero displacement')

fields = ['class',
          'from',
          'to',
          'date',
          'time',
          'pfname',
          'plname',
          'pid',
          'pemail',
          'ppwd']

s = {}
for x in fields:
    s[x] = form.getvalue(x)

print(s)

conn = pymysql.connect(
    db='cse311db',
    user='trk',
    passwd='',
    host='localhost',
    cursorclass=pymysql.cursors.DictCursor
)