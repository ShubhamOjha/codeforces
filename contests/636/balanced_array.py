t = int(input())
for _ in range(t):
    n = int(input())
    if (n/2)%2==0:
        print("YES")
        left_a = list(range(2,n+1,2))
        right_a = list(range(1,n-1,2))
        rem = sum(left_a) - sum(right_a)

        print(*left_a,*right_a, rem)
    else:
        print("NO")