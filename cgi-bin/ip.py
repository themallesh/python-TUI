#!/usr/bin/python3

import subprocess as s
import cgi

print("Content-type:text/html")
print()

#form = cgi.FieldStorage()
#data=form.getvalue("fldr")

out=s.getoutput("ifconfig")
print("<pre><h3>")
print(out)
print("</h3></pre>")

