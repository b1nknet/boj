board = []
minimum, cntB, cntW = 80, 0, 0
N, M = map(int, input().split())

for _ in range(N): board.append(list(input()))

for i in range(N - 7):
    for j in range(M - 7):
        cntB, cntW = 0, 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == 'B': cntW += 1
                    else: cntB += 1
                else:
                    if board[a][b] == 'B': cntB += 1
                    else: cntW += 1
        minimum = min(minimum, cntB, cntW)

print(minimum)