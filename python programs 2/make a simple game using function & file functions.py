import random

def game():
    print("you are playing the game......")
    score=random.randint(1,99)
    #fitch the high score
    with open("high score.txt") as f:

        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

        print(f"your score:{score}")
        if(score>highscore):
            #write this highscore to the file
            with open("high score.txt","w") as f:
                f.write(str(score))

    return score


game()