apple = 0
banana = 0

for i in range(3):
    apple += int(input())*(3-i)

for i in range(3):
    banana += int(input())*(3-i)
    
if apple == banana: print('T')
else: print('A' if apple > banana else 'B')