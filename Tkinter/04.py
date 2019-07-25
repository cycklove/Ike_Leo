import  re

p = re.compile(r'[^A-Za-z0-9]')

m =p.match("fasf")
m2 =p.match("!!")
print(m)
print(m2)