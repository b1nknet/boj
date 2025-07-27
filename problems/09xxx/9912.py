import math

def solve():
    n = int(input())
    permutation = list(map(int, input().split()))
    available_numbers = list(range(n))
    rank = 0
    for i in range(n):
        current_num = permutation[i]
        num_smaller = available_numbers.index(current_num)
        available_numbers.remove(current_num)
        rank += num_smaller * math.factorial(n - 1 - i)
    print(rank + 1)

solve()