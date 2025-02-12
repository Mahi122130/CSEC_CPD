def min_shovels(k, r):
    for x in range(1, 11):
        total_cost = x * k
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return x
    return 10

k, r = map(int, input().split())
print(min_shovels(k, r))
