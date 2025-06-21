import sys

code = {
    "063": 0,
    "010": 1,
    "093": 2,
    "079": 3,
    "106": 4,
    "103": 5,
    "119": 6,
    "011": 7,
    "127": 8,
    "107": 9,
}

code_rev = {v: k for k, v in code.items()}


def num(m):
    n = ""
    for i in range(0, len(m), 3):
        n += str(code[m[i : i + 3]])
    return int(n)


while True:
    N = sys.stdin.readline().rstrip()
    if N == "BYE":
        break

    sp = N.split("+")
    A = sp[0]
    B = sp[1][: len(sp[1]) - 1]

    A_num = num(A)
    B_num = num(B)
    C_num = str(A_num + B_num)

    C = ""
    for i in C_num:
        C += code_rev[int(i)]
    print(N + C)