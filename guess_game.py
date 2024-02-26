from random import randint

answer = randint(1, 10)
def guesses_game(answer, user):
    while True:
        print(answer)
        try:
            user = int(input("Enter number between 1 to 10: "))
            if 0 < user < 11:
                if user == answer:
                    print("You're a special being, keep it up")
                    break
                else:
                    print("Wrong try again dude")
        except ValueError:
            print("Ahh!. Enter a number nut head")
