#lets us play a number game using random module
import random
print("choose the game 1--->number gussing or 2---->rock-paper-scissor")
choice=int(input())
if(choice==1):
    times=int(input("enter how many times you repeat the game:"))
    for j in range(times):
        machine=random.randint(1,10)
        guess=int(input("enter a value in 1-10"))
        while machine!=guess:
            if guess<machine:
                print("oops num is small enter again")
                guess=int(input("enter number"))
            elif guess>machine:
                print("oops num is larger enter again")
                guess=int(input("enter number"))
            else:
                break
        print("Hayyyyyyyyyyyyyyy u won the game")
elif(choice==2):
    times=int(input("enter how many times you repeat the game:"))
    for j in range(times):
        print("choose one from rock-paper-scissor")
        elements=["rock","paper","scissor"]
        machine=random.choice(elements)
        guess=input()
        if machine=="rock" and guess=="rock":
            print("draw")
        elif machine=="rock" and guess=="paper":
            print("ewww you won the game")
        elif machine=="rock" and guess=="scissor":
            print("ohhh nooo u loose the game")
        elif machine=="paper" and guess=="rock":
            print("ohhh nooo u loose the game")
        elif machine=="paper" and guess=="paper":
            print("draw")
        elif machine=="paper" and guess=="scissor":
            print("heyyy u won the game")
        elif machine=="scissor" and guess=="rock":
            print("awesome u won  the game")
        elif machine=="scissor" and guess=="scissor":
            print("draw")
        elif machine=="scissor" and guess=="paper":
            print("sorry u loose the game")
        else:
            print("enter proper one given above")
else:
    print("enter either 1 or 2 options")
