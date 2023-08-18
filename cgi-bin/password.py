#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()


print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("passwd")



if data=="Linux":
    print("<h1>Your password is correct, click on redirect to go further</h1>")
    print("<form action='/main.html' >")
    print("<h3><button type='submit' class='submit-btn'>Redirect</button></h3>")

else:
    print("<h1>Wrong password</h1>")
    print("<form action='/pass.html' >")
    print("<h2><button type='submit' class='submit-btn'>Retry</button></h2>")

