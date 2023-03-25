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

s = S()
# dp[i][j] は i 文字目から j 文字目からに含まれる文字数
l = len(s)
dp = [[1 << int(c) for c in s] for _ in range(l)]
for j in range(1, l):
  k = int(s[j])
  dp[0][j] = dp[0][j-1] ^ (1 << k)
for i in range(1, l):
  k = int(s[i-1])
  for j in range(i, l):
    dp[i][j] = dp[i-1][j] ^ (1 << k)

res = 0
for i in range(0, l):
  for j in range(i, l):
    if dp[i][j] == 0:
      res += 1
print(res)
