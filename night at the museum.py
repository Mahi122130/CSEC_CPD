def min_moves_to_print(s):
    total_moves = 0
    current_position = ord('a')  

    for char in s:
        target_position = ord(char)
        direct_distance = abs(target_position - current_position)
        wrap_around_distance = 26 - direct_distance
        total_moves += min(direct_distance, wrap_around_distance)
        current_position = target_position  

    return total_moves

s = input().strip()  
print(min_moves_to_print(s))
