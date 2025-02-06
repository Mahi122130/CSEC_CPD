def count_guest_uniform_changes(n, teams):
    count = 0
    for i in range(n):  
        for j in range(n):  
            if i != j and teams[i][0] == teams[j][1]:
                count += 1
    return count
n = int(input()) 
teams = [tuple(map(int, input().split())) for _ in range(n)]  

print(count_guest_uniform_changes(n, teams))
