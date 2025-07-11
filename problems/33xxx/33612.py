n = int(input())
a=2024
b=8
b+=7*(n-1)
a=a+(b//12)
if b%12==0: 
    a-=1
    b=12
else: b%=12
print(a,b)