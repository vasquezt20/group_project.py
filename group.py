import random
player =[]
computer = []

def create():
    print("""Welcome to 21 python style game. Rules: You are going to get a number randomly from 1-10 twice.
    Than, you are going to decide if you want 1 extra random number , but if after adding that extra number 
    to the 2 previous numbers you got a total more than 21, you automatically lose. Your goal is to get closer to
    21, because the computer will also get 2 random number, and you need to get a higher total if you want to win.
    The computer can not get over 21.If you win you will receive double of what you bet, if you lose, you will only lose
    the money you bet.""")
    print(" To start the game you need to add money to your bank")
    print("Enter the amount of money you want in your bank\n>")
    return int(input())

def money_bet():
    print("Enter the amount of money you want to bet\n>")
    return int(input())


def roll_dice():
    roll = random.randint(1,11)
    return roll

def player_list():
    bank = create()
    bet = money_bet()
    for i in range(0,1):
        x = roll_dice()
        y = roll_dice()
        player.append(x)
        player.append(y)
        total_player = int(sum(player))
        print(f'Your first number is > {x}')
        print(f'Your second number is > {y}')
        answer = input("Do you want one more number ? Yes or No?\n>")
        if answer == "Yes":
            for i in range(0,1):
                z = roll_dice()
                player.append(z)
                total_player = int(sum(player))
                print(f"{z}")
                print(f" Your total is {total_player}")
        else:
            print(f" Your total is {total_player}")
    for i in range(0,1):
        a = roll_dice()
        b = roll_dice()
        computer.append(a)
        computer.append(b)
        total_computer = int(sum(computer))
        print(f"The computer got {total_computer} ")
    if total_player > 21:
        print("You lose because your total is more than 21.")
        bank = bank - bet
        print(f"Your total bank is {bank}")
    elif total_player > total_computer:
        print("You win!")
        bank = bank + 2 * bet
        print(f"Your total bank is {bank}")
    elif total_player < total_computer:
        print("You lose!")
        bank = bank - bet
        print(f"Your total bank is {bank}")

    choice = input("Dou you want play again? Yes or No?")
    if choice == "Yes":
        bet = money_bet()
        player.clear()
        computer.clear()
        for i in range(0,1):
            x = roll_dice()
            y = roll_dice()
            player.append(x)
            player.append(y)
            total_player = int(sum(player))
            print(f'Your first number is > {x}')
            print(f'Your second number is > {y}')
            answer = input("Do you want one more number ? Yes or No?\n>")
            if answer == "Yes":
                for i in range(0,1):
                    z = roll_dice()
                    player.append(z)
                    total_player = int(sum(player))
                    print(f"{z}")
                    print(f"Total {total_player}")
            else:
                print(f"Your total is {total_player} ")
        for i in range(0,1):
            a = roll_dice()
            b = roll_dice()
            computer.append(a)
            computer.append(b)
            total_computer = int(sum(computer))
            print(f"The computer got {total_computer} ")
        if total_player > 21:
            print("You lose")
            bank = bank - bet
            print(f"Your total bank is {bank}")
        elif total_player > total_computer:
            print("You won!")
            bank = bank + 2 * bet
            print(f"Your total bank is {bank}")
        elif total_player < total_computer:
            print("You lose!")
            bank = bank - bet
            print(f"Your total bank is {bank}")

        choice = input("Dou you want play again? Yes or No?")

        if ( bet > bank):
            print("You dont have that money available,the game will end.")
            bet = 0
        else:
            print("Bye Bye")
            bet = 0

player_list()
