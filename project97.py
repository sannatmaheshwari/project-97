import random
print("number guessing game")
number = random.randint(1,9)
chances = 0
print("guess a number between 1 to 9")
while chances<5:
    guess = int(input("enter a number="))
    if guess ==number:
        print("congratulations you won")
        break
    elif guess<number:
        print("your guess was too low")
    else:
        print("your guess was too high")
    chances+=1
if not chances<5:
    print("you loose,the number is ",number)