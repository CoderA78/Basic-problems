n=20
number_of_guesses=1
print("No. of guess is limited to 9 times.")
while (number_of_guesses <=9):
    i=int(input("Guess the number: \n"))
    if i>n:
        print("You have entered greater value, Please enter a lesser one! \n")
    elif i<n:
        print("You have entered lesser value, Please enter a greater one! \n")
    else:
        print("Congratulations! You Won! \n")
        print(number_of_guesses, "no. of guess, you took to finish!")
        break
    print(9 - number_of_guesses, "No. of guesses left!")
    number_of_guesses= number_of_guesses+1

if(number_of_guesses>9):
    print("GAME OVER")



