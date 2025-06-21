import sys
S = sys.stdin.readline().strip()
result = 0 
for start in range(52):
    for end in range(start+1,52):
        if S[start] == S[end]:
            cows = S[start:end+1]
            for i in cows:
                if cows.count(i) == 1:
                    result += 1
            break
print(result // 2)