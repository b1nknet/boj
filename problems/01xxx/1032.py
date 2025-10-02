n = int(input())
firstWord = list(input())
firstWordLen = len(firstWord)
for i in range(n - 1):
    otherWords = list(input())
    for j in range(firstWordLen):
        if firstWord[j] != otherWords[j]:
            firstWord[j] = '?'

print(''.join(firstWord))