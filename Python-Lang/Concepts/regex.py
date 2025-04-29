import re
name = "peddireddy hari vardhan reddy learning devops technologies"
print(name)
stname = "peddireddy"
print(re.findall("\w",name,re.ASCII))
print(re.findall(stname,name))

chrs = "[peddi]"
print(re.findall(chrs,name))