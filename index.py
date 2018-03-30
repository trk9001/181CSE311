#! /usr/bin/env python

import cgitb
import pymysql

cgitb.enable()

print('Content-Type: text/html; charset=utf-8')
print()

print("""
<!DOCTYPE html>

<meta charset="utf-8">
<title>Home | Katair Air</title>

<link rel="stylesheet" href="/styles/style.css">
<link rel="icon" href="favicon.ico">

<header>
    <h1>Katair Air</h1>
    <hr>
    <nav>
        <a href="#" class="active">Home</a>⬥
        <a href="/ops/bookflight.html" class="">Book a flight</a>⬥
        <a href="#" class="">Flight query</a>⬥
        <a href="#" class="">Log in</a>
    </nav>
    <hr>
</header>

<main>
    <p>This is the main content.</p>

    <p>Lorem ipsum dolor sit amet consectetur adipiscing, elit fames tristique mollis pharetra, massa morbi egestas consequat iaculis. Aptent torquent auctor fusce potenti suspendisse rutrum praesent neque placerat lectus dis, lacus sem feugiat mus faucibus nullam in facilisi consequat aliquam. Rhoncus ante convallis montes natoque facilisi sed velit pellentesque imperdiet vel augue eget facilisis, diam tincidunt ad pulvinar et felis tristique duis cursus erat ultrices eu. Eleifend duis suscipit molestie quam laoreet morbi sapien interdum, parturient lacus suspendisse risus tempor quis bibendum velit tortor, pulvinar pellentesque augue fringilla justo feugiat habitant. Faucibus lacinia ac id arcu montes fames dictum, congue aptent ad ante orci suspendisse, malesuada sollicitudin hac enim tellus integer.</p> <p>Pulvinar tempus nunc felis dis tortor ultricies gravida hac placerat diam ornare, iaculis senectus dictum laoreet donec netus massa leo eget. Laoreet placerat nostra cubilia fermentum ultrices vivamus cum blandit enim lobortis, volutpat vehicula lectus ornare hendrerit etiam primis semper vestibulum, faucibus nunc eros nulla et tempus iaculis magna posuere. Nec non mattis mi neque magnis ac tristique cubilia varius morbi, sem cum integer vestibulum curae montes cursus cras accumsan, metus semper auctor maecenas magna parturient rhoncus commodo senectus. Nulla nec ornare vel mus fringilla nullam auctor, tincidunt habitant lacinia facilisis eget netus nisi inceptos, taciti orci vulputate elementum viverra id. Nascetur arcu eget faucibus auctor aliquet neque est per placerat imperdiet orci, cursus aptent augue platea habitasse curabitur sagittis dignissim ac viverra, suscipit varius lacus elementum hendrerit luctus in sapien inceptos dapibus.</p> <p>Eleifend dictumst per risus velit in, massa parturient nec suspendisse varius ad, volutpat torquent felis quis. Dignissim ultrices potenti fusce facilisis iaculis quam eros volutpat, eget conubia vehicula natoque auctor eu diam, interdum nec vulputate ridiculus risus a id. Himenaeos ultrices semper vestibulum cubilia sociis commodo lacinia orci, nulla duis pretium euismod aptent malesuada curae dapibus, mattis augue suscipit cursus fringilla ante luctus. Platea nisl velit auctor torquent lobortis ante posuere, senectus porttitor duis nullam per ac diam aptent, molestie orci nisi quis natoque gravida. Auctor egestas sed magnis primis sociis, semper sollicitudin mi. Ornare aliquet venenatis scelerisque vel porttitor imperdiet accumsan ante, convallis quam magnis nec tincidunt vestibulum class duis felis, senectus per feugiat torquent elementum cursus nascetur.</p>
</main>

<footer>
    <hr>
    <p><i>Created with ♥ for CSE311</i></p>
</footer>
""")

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
