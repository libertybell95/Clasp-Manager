# Gets a list of current standalone scripts available

import subprocess # Used for calling/invoking CMD processes
import re # Regular Expressions (https://docs.python.org/3.7/library/re.html)
import sqlite3 # SqlLite (https://docs.python.org/3.7/library/sqlite3.html)

cmdOut = subprocess.check_output("clasp list", shell=True).decode("UTF-8") # Fetches raw console output of 'clasp list'

initRe = re.findall(r"1G(\w.[\s\S]*)", cmdOut)[0]# Filters out unwanted characters so only script name and URLs are found
scriptInfoRe = re.finditer(r"(.*?)\s{2}.*\s.*d/(.*)/", initRe)

for i in scriptInfoRe:
    print(i.group(1)+" | "+i.group(2))