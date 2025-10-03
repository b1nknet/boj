import sys

input = sys.stdin.readline

n = int(input())

arr = [0] * 10001

ans = 0
mxcnt = 0

for _ in range(n):
    x = int(input())
    arr[x] += 1
    
    if arr[x] > mxcnt or (arr[x] == mxcnt and x < ans):
        mxcnt = arr[x]
        ans = x

print(ans)