input = __import__('sys').stdin.readline

n = int(input())
f = int(input())

a = (n // 100) * 100

while a % f != 0: a += 1
print(str(a)[-2:])