n, x = list(map(int, input().split()))
A = list(map(int, input().split()))
A_set = set(A)
is_awesome = False

for num in A:
    desired_num = x - num
    if desired_num in A_set:
        if desired_num == num and A.count(num) == 1:
            continue
        is_awesome = True
        break

if is_awesome:
    print("YES")
else:
    print("NO")
