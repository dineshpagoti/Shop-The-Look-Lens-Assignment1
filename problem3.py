def last_man_standing(n):
    # Step 1: Initialization
    people = list(range(1, n + 1))
    
    # Step 2: Elimination Process
    while len(people) > 1:
        # Remove every second person
        people = people[::2]
    
    # Step 3: Finding the Survivor
    return people[0]

# Example usage:
n = 100
last_survivor = last_man_standing(n)
print("The last man standing is:", last_survivor)
