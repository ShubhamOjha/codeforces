def get_positive_sub_seq(current_index, n):
    start_index = current_index
    while current_index<len(n):
        if n[current_index]>0:
            current_index += 1
        else:
            break
    return (max(n[start_index:current_index]), current_index-1)


def get_negative_sub_seq(current_index, n):
    start_index = current_index
    while current_index<len(n):
        if n[current_index]<0:
            current_index += 1
        else:
            break
    return (max(n[start_index:current_index]), current_index-1)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    current_index = 0
    sum = 0
    while(current_index<n):
        e = a[current_index]
        if e>0:
            max_num,current_index = get_positive_sub_seq(current_index, a)
        elif e<0:
            max_num,current_index = get_negative_sub_seq(current_index, a)
        sum += max_num
        current_index += 1
    print(sum)

