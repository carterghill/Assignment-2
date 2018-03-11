from Game import Game
import sys

ai1 = False
ai2 = False

if len(sys.argv) > 1:

    if "-ai1" in sys.argv:
        ai1 = True
    if "-ai2" in sys.argv:
        ai2 = True

else:

    print("\nAvailable game modes:\n")

    print(" 1. Human vs Human")
    print(" 2. AI vs Human")
    print(" 3. Human vs AI")
    print(" 4. AI vs AI\n")

    x = int(input("Select mode by #: "))
    while x < 1 and x > 4:
        x = int(input("Try again, human: "))

    if x == 2:
        ai1 = True
    elif x == 3:
        ai2 = True
    elif x == 4:
        ai1 = True
        ai2 = True

game = Game(ai1, ai2)
game.play()
