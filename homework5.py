lifecounter=30

while lifecounter > 0:
    print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
    answer1 = input()
    if answer1 == "S":
        print("correct")
        print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
        answer2 = input()
        if answer2 == "S":
            print("correct")
            print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
            answer3 = input()
            if answer3 == "N":
                print("correct")
                print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
                answer4 = input()
                if answer4 == "W":
                    print("correct")
                    print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
                    answer5 = input()
                    if answer5 == "E":
                        print("correct")
                        print("You are in the magic maze, which way would you like to go? (N,S,E,W)")
                        answer6 = input()
                        if answer6 == "S":
                            print("CONGRATULATIONS, YOU MADE IT OUT OF THE MAZE IN ", lifecounter, "MOVES! :)")
                            break
                        else:
                            print("incorrect")
                            lifecounter = lifecounter - 1
                            if lifecounter == 0:
                                print("You are dead")
                            else:
                                print("You have ", lifecounter, "lifes left")

                    else:
                        print("incorrect")
                        lifecounter = lifecounter - 1
                        if lifecounter == 0:
                            print("You are dead")
                        else:
                            print("You have ", lifecounter, "lifes left")
                else:
                    print("incorrect")
                    lifecounter = lifecounter - 1
                    if lifecounter == 0:
                        print("You are dead")
                    else:
                        print("You have ", lifecounter, "lifes left")
            else:
                print("incorrect")
                lifecounter = lifecounter - 1
                if lifecounter == 0:
                    print("You are dead")
                else:
                    print("You have ", lifecounter, "lifes left")
        else:
            print("incorrect")
            lifecounter = lifecounter - 1
            if lifecounter == 0:
                print("You are dead")
            else:
                print("You have ", lifecounter, "lifes left")
    else:
        print("incorrect")
        lifecounter = lifecounter - 1
        if lifecounter == 0:
            print("You are dead")
        else:
            print("You have ", lifecounter, "lifes left")