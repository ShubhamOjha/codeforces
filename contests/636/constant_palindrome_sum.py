from collections import Counter
import sys
 
sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
 
def main():
    for _ in range(II()):
        n,k=MI()
        aa=LI()
        cnt=[0]*(2*k+2)
        for i in range(n//2):
            a,b=aa[i],aa[n-1-i]
            if a>b:a,b=b,a
            cnt[0]+=2
            cnt[a+1]+=-1
            cnt[a+b]+=-1
            cnt[a+b+1]+=1
            cnt[b+k+1]+=1
        for i in range(2*k+1):cnt[i+1]+=cnt[i]
        print(min(cnt))
 
main()
