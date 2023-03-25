# --- template ---
import bisect,collections,copy,heapq,itertools,math,numpy,string,decimal
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def BOOLPRINT(B, OUT): print(OUT[0] if B else OUT[1])
def YESNO(B): BOOLPRINT(B, ('YES', 'NO'))
def YesNo(B): BOOLPRINT(B, ('Yes', 'No'))
def sqrt(x): return decimal.Decimal(x) ** decimal.Decimal('0.5')
# -----------------
h, w = LI()
b = []
for _ in range(h):
  b.append(S())
brk = [[False] * w for _ in range(h)]
for y in range(h):
  for x in range(w):
    here = b[y][x]
    if here not in ['.', '#']:
      dist = int(here)
      for y2 in range(h):
        for x2 in range(w):
          if abs(x - x2) + abs(y - y2) <= dist:
            brk[y2][x2] = True

for y in range(h):
  for x in range(w):
    print('.' if brk[y][x] else b[y][x] , end='')
  print()

