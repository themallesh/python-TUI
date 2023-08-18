#!/usr/bin/python3

import os
import subprocess
import cgi

print("Content-type:text/html")
print()


print("<pre><h1>")
out=subprocess.getoutput("date")
print(out)
print("</h1></pre>")

