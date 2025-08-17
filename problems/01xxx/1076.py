colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

result = 0

result += colors.index(input()) * 10
result += colors.index(input())
result *= 10**(colors.index(input()))

print(result)