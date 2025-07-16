import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

anger = 0
total = 0

for weather in arr:
    if weather == 1:
        anger += 1
    else: anger -= 1
    total += anger

print(total)