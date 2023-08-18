#!/usr/bin/python3

import os
import subprocess
import cgi

print("Content-type:text/html")
print()


print("<pre><h3>")
out=subprocess.getoutput("cal")
print(out)
print("</h3></pre>")


