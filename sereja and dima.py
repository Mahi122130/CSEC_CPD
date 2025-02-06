def sereja_and_dima(n, cards):
    left, right = 0, n - 1  
    sereja_score, dima_score = 0, 0  
    turn = True  
    
    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        if turn:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card
        
        turn = not turn  
    
    print(sereja_score, dima_score)


n = int(input())
cards = list(map(int, input().split()))

sereja_and_dima(n, cards)
