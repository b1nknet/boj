import sys
input = sys.stdin.readline
total = 300
for _ in range(4): 
    total += int(input())
print("No" if total > 1800 else "Yes")