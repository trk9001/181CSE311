#! /var/www/trk/venv/bin/python

import cgi
import cgitb
import html
import sys

import passlib
import pymysql

from templates.master import *

cgitb.enable()

print('Content-Type: text/html')
print()

print(head.format('Error'))
print(header.format(nav_0))

form = cgi.FieldStorage()
mal = False

if len(form) < 10:
    print(f'<p><strong>Error:</strong> Expected 10 values, received {len(form)}'
    '.</p>\n')
    mal = True

if form.getvalue('from') == form.getvalue('to'):
    print('<p><strong>Error:</strong> Departure and destination points are '
    'the same.</p>\n')
    man = True

if mal:
    print(footer)
    sys.exit(0)

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

conn = pymysql.connect(
    db='cse311db',
    user='trk',
    passwd='',
    host='localhost',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as c:
    c.execute('select max(id) from tickets')
    max_ticket_id = c.fetchone()['max(id)']

    


print('<p>' + html.escape(str(s)) + '</p>\n')
print(footer)
