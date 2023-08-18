#!/usr/bin/python3

import subprocess
import cgi

print("Content-type:text/html")
print()

form = cgi.FieldStorage()
data1=form.getvalue("usr")
data2=form.getvalue("passwd")


out1=subprocess.getoutput("sudo useradd {} -p {}".format(data1,data2))


print("<pre><h1>")
print("Created {} successfully".format(data1))
print("</h1></pre>")

