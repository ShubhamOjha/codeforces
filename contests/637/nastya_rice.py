t = int(input())
for _ in range(t):
    n , a, b, c, d = list(map(int, input().split(' ')))
    min_grain = a-b
    max_grain = a+b
    min_pkg= c-d
    max_pkg = c+d
    r1 = min_pkg/min_grain
    r2 = min_pkg/max_grain
    r3 = max_grain/min_grain
    r4 = max_grain/max_grain
    if n in [r1,r2,r3,r4]:
        print('Yes')
    elif isinstance(r1, int) and min_pkg%((r1*min_grain)+(n-r1)*max_grain)==0:
        print('Yes')
    elif isinstance(r2, int) and min_pkg%((r2*max_grain)+(n-r2)*min_grain)==0:
        print('Yes')
    elif isinstance(r3, int) and max_pkg%((r3*min_grain)+(n-r3)*max_grain)==0:
        print('Yes')
    elif isinstance(r4, int) and max_pkg%((r4*max_grain)+(n-r4)*min_grain)==0:
        print('Yes')
    else:
        print('No')