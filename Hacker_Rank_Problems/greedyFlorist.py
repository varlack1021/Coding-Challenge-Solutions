def getMinimumCost(k, c):
    current_number_purchases = 0
    check = 0
    number_of_friends = k
    cost_array = c
    cost_array.sort()
    minimum_cost = 0
    
    for i in range(1, len(cost_array) + 1):
        original_cost = cost_array[-i]
    
        minimum_cost += original_cost * (1 + current_number_purchases)
        check += 1
        if check == number_of_friends:
            current_number_purchases += 1
            check = 0
    return minimum_cost