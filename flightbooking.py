#! /var/www/trk/venv/bin/python

import cgi
import cgitb
import html
import passlib
import pymysql

from templates.master import *

cgitb.enable()

print('Content-Type: text/html')
print()

print(head.format('Error'))
print(header.format(nav_0))

form = cgi.FieldStorage()

if len(form) < 10:
    print(f'<p><strong>Error:</strong> Expected 10 values, received {len(form)}'
    '.</p>\n')

if form.getvalue('from') == form.getvalue('to'):
    print('<p><strong>Error:</strong> Departure and destination points are '
    'the same.</p>\n')

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

print('<p>' + html.escape(str(s)) + '</p>\n')
print(footer)
