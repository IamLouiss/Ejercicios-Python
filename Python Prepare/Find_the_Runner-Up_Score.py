n = int(input())
arr = list(map(int, input().split()))

campeon = subcampeon = -100;
for i in arr:
    print(i)
    if i > campeon:
        subcampeon = campeon
        campeon = i
    elif subcampeon < i < campeon:
        subcampeon = i

print(subcampeon)