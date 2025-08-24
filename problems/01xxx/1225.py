import sys
input = sys.stdin.readline

a, b = input().split()
total = 0

for i in range(len(a)):
    for j in range(len(b)):
        total += int(a[i]) * int(b[j])

print(total)