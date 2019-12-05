import random

options = "NSEW"
list_main = [random.choice(options) for i in range(6)]
list_game = list_main[:]
moves = 0
hp = 3
day = "tuesday"
print(" Hello {}. Today is {}".format("Chloe", day))

print("You are trapped in the magic maze!")


def remove_hp(hp_down):
    if hp_down > 1:
        print("{} lives left!".format(hp_down))
    else:
        print("{} life left!".format(hp_down))
    return hp_down - 1


while True:
    if moves % 10 == 0:
        hp = remove_hp(hp)
    if not hp:
        print("YOU DIED!")
        break
    if not list_game:
        print("YOU ESCAPED!\nIn {} moves".format(moves))
        break
    print("\n{} rooms left!".format(list_game.__len__()))
    move = input("Enter a move [N/S/E/W] >> ").upper()
    if move not in options:
        print("Invalid move!")
        continue
    moves += 1
    if move == list_game[0]:
        print("Continue!")
        list_game.remove(list_game[0])
    else:
        print("WRONG PATH")
        list_game = list_main[:]
        hp = remove_hp(hp)
