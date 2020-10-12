a='@@mickey##'
print(len(a))
b=a.lstrip('@')
print(len(b))
c=a.rstrip('#')
print(len(c))
print(len(a.lstrip('@').rstrip('#')))
print(a.lstrip('@').rstrip('#'))