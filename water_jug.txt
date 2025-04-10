def water_jug_solution(large_capacity, small_capacity, target):
    large, small = 0, 0 
    steps = [] 

    print(f"Enter target amount of water: {target}") 

    while large != target and small != target:
        steps.append(f"Large Jug: {large}, Small Jug: {small}")
    
        if large == 0:
            large = large_capacity
    
        elif small < small_capacity:
            transfer = min(large, small_capacity - small)
            large -= transfer
            small += transfer
    
        elif small == small_capacity:
            small = 0
    
        elif large == large_capacity:
            small = 0


    steps.append(f"Large Jug: {large}, Small Jug: {small}")
    steps.append("Reached the target!")


    print("\n".join(steps))


if __name__ == "__main__":

    LARGE_JUG_CAPACITY = 5
    SMALL_JUG_CAPACITY = 4

    target = int(input()) 

    if target > max(LARGE_JUG_CAPACITY, SMALL_JUG_CAPACITY):
        print("Target cannot be greater than both jugs' capacities!")
    else:
        water_jug_solution(LARGE_JUG_CAPACITY, SMALL_JUG_CAPACITY, target)
