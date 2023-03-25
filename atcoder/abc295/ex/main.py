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