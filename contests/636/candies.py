t = int(input())
for _ in range(t):
    n = int(input())
    k = 2
    while True:
        gp_sum = (2**k) -1
        if n%gp_sum == 0:
            x = n/gp_sum
            print(int(x))
            break
        k += 1
