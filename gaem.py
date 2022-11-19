#Just a fun little game I made durning lunch one day. Try to guess the number!

import random

def ttime(xe):
    try:
        y = int(xe)
        return y
    except:
        xep = input("Input integers only. ")
        return ttime(xep)

def guezz():
    guess = ttime(input("Guess a number from from 1-100 "))
    return guess

def game():
    number_list = []
    gnum = 1
    first_numb = random.randint(1, 100)
    gin = guezz()

    while gin != first_numb:
        number_list.append(gin)
        gnum = gnum + 1
        if gin > first_numb:
            print("Your guess was too high.")
        else:
            print("Your guess was too low.")
        print("Your past guesses are", number_list)
        gin = guezz()
    number_list.append(gin)
    print("You got the correct answer in", gnum, "guesses! "
                                               "\n You guessed" , number_list)


while __name__ == "__main__":

    run = game()

    er = input("Input 0 to exit, or other to play again")
    if er == "0":
        exit()



