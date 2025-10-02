n, k = map(int, input().split())
answer = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    answer += 2 ** idx
    n += 2 ** idx
print(answer)