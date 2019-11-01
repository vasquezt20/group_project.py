import random


def guessing():

    print("Hi! I'm thinking of a random number between 1 and 20. You have 5 tries to guess.")

    random_number = random.randrange(1, 21)

    user_attempt_number = 1

    user_guess = 0

    while user_guess != random_number and user_attempt_number < 5:

        print("Guess #", user_attempt_number)
        user_input_text = input("Guess what number I am thinking of: ")
        user_guess = int(user_input_text)

        if user_guess > random_number:
            print("Too high.")
        elif user_guess < random_number:
            print("Too low.")
        else:
            print("You got it!")

        user_attempt_number += 1

    if user_guess != random_number:
        print("That's enough. The number was " + str(random_number) + ".")

guessing()
