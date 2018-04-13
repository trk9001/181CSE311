#! /var/www/trk/venv/bin/python

import cgi
import cgitb

import pymysql
from passlib.hash import pbkdf2_sha256

from templates.master import *

cgitb.enable()

print('Content-Type: text/html')
print()

print(head.format('Feedback'))
print(header.format(nav_0))

mal = False
form = cgi.FieldStorage()

if len(form) < 10:
    print(f'<p><strong>Error:</strong> Expected 10 values, received {len(form)}.</p>\n')
    mal = True

if form.getvalue('from') == form.getvalue('to'):
    print('<p><strong>Error:</strong> Departure and destination points are the same.</p>\n')
    mal = True

if mal:
    pass

else:
    hash = pbkdf2_sha256.using(salt_size=0).hash

    fieldnames = ['class',
              'from',
              'to',
              'date',
              'time',
              'pfname',
              'plname',
              'pid',
              'pemail',
              'ppwd']

    fields = {}
    for x in fieldnames:
        fields[x] = form.getvalue(x)

    conn = pymysql.connect(
        db='cse311db',
        user='trk',
        passwd='',
        host='localhost',
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn.cursor() as c:
        sql = 'select id ' \
              'from flights ' \
              'where `from` = "{}" and `to` = "{}" and time = "{}"'

        if c.execute(sql.format(fields['from'], fields['to'], fields['time'])) == 0:
            mal = True

    if mal:
        pass

    else:
        with conn.cursor() as c:
            c.execute('select max(id) from tickets')
            last_ticket_id = c.fetchone()['max(id)']

            pid = int(fields['pid'])
            ticket_id = last_ticket_id + 1;
            pfname = fields['pfname']
            plname = fields['plname']
            pemail = fields['pemail']
            ppwd = hash(fields['ppwd'])

            c.execute('insert into passengers (passportnumber, ticket_id, firstname, lastname, email, passwordhash) '
                      'values ({}, {}, "{}", "{}", "{}", "{}")'.format(pid, ticket_id, pfname, plname, pemail, ppwd));

        conn.commit()

        with conn.cursor() as c:
            c.execute('select max(id) from tickets')
            ticket_id = c.fetchone()['max(id)'] + 1

            sql = 'select id from flights where `from` = "{}" and `to` = "{}" and `time` = "{}"'

            c.execute(sql.format(fields['from'], fields['to'], fields['time']))
            flight_id = c.fetchone()['id']

            c.execute('select seats from flights where id = "{}"'.format(flight_id))
            seat = 320 - c.fetchone()['seats'] + 1

            c.execute('select price from pricing where class = "{}" and time = "{}"'.format(fields['class'], fields['time']))
            price = c.fetchone()['price']

            pid = int(fields['pid'])
            class_ = fields['class']
            date_ = fields['date']

            c.execute('insert into tickets (flight_id, passenger_id, seat, class, price, `date`) '
                      'values ("{}", {}, {}, "{}", {}, "{}")'.format(flight_id, pid, seat, class_, price, date_))

            c.execute('update flights set seats = {} where id = "{}"'.format((320 - seat), flight_id))

        conn.commit()

        print('<p><strong>Success:</strong> Your flight has been booked.</p>\n')

    conn.close()

print(footer)
