#!python3

import json

f = open('data.csv','r')
data = f.read().strip()

decoded = json.loads(data)
print( type(decoded) )
print( decoded )