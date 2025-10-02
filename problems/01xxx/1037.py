n = int(input())
if n == 1: print(int(input()) ** 2)
else:
    a = list(map(int, input().split()))
    a.sort()
    print(a[0] * a[-1])