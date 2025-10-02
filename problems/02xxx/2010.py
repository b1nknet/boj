input = __import__('sys').stdin.readline
total = 0
n = int(input())
for _ in range(n):
    total += int(input())
    
print(total - n + 1)