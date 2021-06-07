import random 
def main():
    user_rps = input("r = rock , p = paper , s = scissor  ")#user input
    user_rps = user_rps.lower() # converting into lower case
    system_rps = random.randint(1,3)
    if system_rps == 1:
        system_rps = "r"
    elif system_rps == 2:
        system_rps = "p"
    else:
        system_rps = "s"
    calculating_score(user_rps,system_rps) # this function will calculate the score

def calculating_score(user_rps,system_rps):
    user_score = 0
    system_score = 0
    if user_rps == "r":
        if system_rps == "p":
            system_score += 1
        elif system_rps == "s":
            user_score += 1
    elif user_rps == "p":
        if system_rps == "r":
            user_score += 1
        elif system_rps == "s":
            system_score += 1
    elif user_rps == "s":
        if system_rps == "p":
            user_score += 1
        elif system_rps == "r":
            system_score += 1
    print(system_rps)
    print(user_score)
    print(system_score)
    
if __name__ == "__main__":
    main()
    
