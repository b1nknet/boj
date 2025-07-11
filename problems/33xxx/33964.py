a, b = map(int, input().split())

x = ''
y = ''

for i in range(a):
    x += '1'
for i in range(b):
    y += '1'
    
print(int(x)+int(y))