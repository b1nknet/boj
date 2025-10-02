import sys

x, y, d, t = map(int, sys.stdin.readline().split())
dist = (x ** 2 + y ** 2) ** 0.5

if dist >= d: ans = min(t * (dist // d) + dist % d, 
                        t * (dist // d + 1), 
                        dist)
else: ans = min(t + (d - dist), 
                2 * t, 
                dist)

print(ans)