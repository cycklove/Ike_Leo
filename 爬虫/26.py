'''
search
'''
import re

s = r'\d+'

pat = re.compile(s)

m = pat.search("one12two34three56")
print(m.group())

m = pat.search("one12two34three56",10,36)
print(m.group())

m = pat.findall("one12two34three56")
print(m)

m = pat.finditer("one12two34three56")

for i in m:
    print(i.group())