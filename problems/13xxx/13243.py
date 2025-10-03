import sys


def main():
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print("0 0")
            return
        nums = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    ans_len = 0
    ans_sum = 0
    cur_len = 0
    cur_sum = 0
    old = float('-inf')

    for x in nums:
        if x >= old:
            cur_len += 1
            cur_sum += x
        else:
            if cur_len > ans_len:
                ans_len = cur_len
                ans_sum = cur_sum
            cur_len = 1
            cur_sum = x
        old = x

    if cur_len > ans_len:
        ans_len = cur_len
        ans_sum = cur_sum

    print(f"{ans_len} {ans_sum}")


if __name__ == "__main__":
    main()