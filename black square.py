def total_calories(calories, s):
    total = 0
    for ch in s:
        total += calories[int(ch) - 1]  
    return total


calories = list(map(int, input().split()))  
s = input().strip()  

print(total_calories(calories, s))
