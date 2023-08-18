#!/usr/bin/python3

import subprocess as s
import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("sftwr")

out=s.getoutput("sudo yum install   {}".format(data))
print("<pre><h2>")
print(out)
print("</h2></pre>")
