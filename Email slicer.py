
# email slicer

a=input('enter your email id')

print(f'user name = {a[:9]} : domain = {a[10:len(a)]}')

b=a.split('@')

print(b[0])
print(b[1])
