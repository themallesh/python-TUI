#!/usr/bin/python3

import subprocess as s
import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("usr")

out=s.getoutput("id {}".format(data))
print("<pre><h1>")
print(out)
print("</h1></pre>")
