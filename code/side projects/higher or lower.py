import random
answer = random.randint(0,1000)
while True:
    if int(input("Guess")) > answer:print("Lower")
    elif int(input("Guess")) < answer:print("Higher")
    else:print("You Win!")