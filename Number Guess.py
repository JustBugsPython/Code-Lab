import random 
while True:
    count = 1
    secret_number = random.randint(1,10)
    num = int(input("Guess a number between 1 and 10, \n"))
    if num == secret_number:
        print("Correct!!, U got it on the first try \n")
    while num != secret_number and count < 5: 
        count += 1
        if count == 5:
            print("Game over!!")
        print("You're wrong, Try again")
        if num > secret_number:
            print("Too High \n")
        else:
            print("Too Low \n")
        num = int(input("Guess Again \n"))
        if num == secret_number:
            print("Correct!!, u guessed it in ",count, "attempts \n")
            break
    ans = str(input("Wanna try again?? \n"))
    if ans.strip().upper() == "YES":
        print("Get ready love, coz the game's gonna start again!! \n")
    else:
        print("Okay bro \n")
        break 