n = int(input())

nums = []
for mask in range(1, 1 << 10):
    num = 0
    for d in range(9, -1, -1):
        if mask & (1 << d):
            num = num * 10 + d
    nums.append(num)

nums.sort()

if n < len(nums):
    print(nums[n])
else:
    print(-1)