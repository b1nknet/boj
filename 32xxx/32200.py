import sys
input = sys.stdin.readline

n,x,y = map(int,input().split())
sws = list(map(int,input().split()))

cnt = 0
least = 0
for sw in sws:
    if sw < x:
        least += sw
    else:
        crnt_cnt = sw // x
        crnt_least = sw % x
        cnt += crnt_cnt
        if crnt_least > crnt_cnt * (y-x):
            least += (crnt_least - crnt_cnt * (y-x))
print(cnt)
print(least)