import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# To clear the screen
clear_screen()

print("***Game Rules***")
print("-----------------")
print("1)Take all the missionaries and cannibals on the left side -- 'YOU WIN'")
print("2) Only One or Two people can travel on the boat from either side.")
print("3) Missionaries on either side should never be less than the Cannibals.")
print("")

boat_side = "RIGHT"
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

print('\U0001f482 =', missionaries_on_left, '\U0001f479 =', cannibals_on_left, '|\U0001f30a\U0001f30a\U0001f30a\U0001f30a\U0001f30a\U0001f6A2 |',
      '\U0001f482 =', missionaries_on_right, '\U0001f479 =', cannibals_on_right)
while True:
    try:
        missionaries = int(
            input("enter the number of missionaries or enter 10 to Quit the game: "))
    except ValueError as ve:
        print("Invalid Move. Please enter a number.")
    else:
        if (missionaries == 10):
            print("You Quit, Game Over.")
            break
        elif (missionaries == 2):
            cannibals = 0
            # print("Missionary = 2")
            # print("Cannibals = 0")
        elif (missionaries == 1):
            cannibals = int(input("enter the numbmer of cannibals..."))
        elif (missionaries == 0):
            cannibals = int(input("enter the numbmer of cannibals..."))
        else:
            print("Invalid Move")
            continue

        if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
            print("Invalid Move")
            continue

        if (boat_side == "RIGHT"):
            if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
                print("Invalid Move")
                continue

            missionaries_on_right = missionaries_on_right-missionaries
            cannibals_on_right = cannibals_on_right - cannibals

            missionaries_on_left += missionaries
            cannibals_on_left += cannibals

            print('\U0001f482 =', missionaries_on_left, '\U0001f479 =', cannibals_on_left, '|\U0001f6A2\U0001f30a\U0001f30a\U0001f30a\U0001f30a\U0001f30a |',
                  '\U0001f482 =', missionaries_on_right, '\U0001f479 =', cannibals_on_right)

            boat_side = "LEFT"
        else:
            if (missionaries_on_left < missionaries or cannibals_on_left < cannibals):
                print("Invalid Move")
                continue

            missionaries_on_left = missionaries_on_left - missionaries
            cannibals_on_left = cannibals_on_left - cannibals

            missionaries_on_right += missionaries
            cannibals_on_right += cannibals

            print('\U0001f482 =', missionaries_on_left, '\U0001f479 =', cannibals_on_left, '|\U0001f30a\U0001f30a\U0001f30a\U0001f30a\U0001f30a\U0001f6A2 |',
                  '\U0001f482 =', missionaries_on_right, '\U0001f479 =', cannibals_on_right)

            boat_side = "RIGHT"

        if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
            print("YOU LOSE!!")
            break

        if (missionaries_on_left == 3 and cannibals_on_left == 3):
            print("YOU WIN")
            break
