x = []

for _ in range(4):
    x.append(int(input()))

if (x[0] in [8, 9]) and (x[3] in [8, 9]) and (x[1] == x[2]):
    print("ignore")
else: print("answer")