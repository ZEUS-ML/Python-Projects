import random
low = int(input("enter lower limit: "))
high = int(input("enter upper limit: "))
key = random.randint(low,high)
attempts = 0
while True:
    guess = int(input("enter guess: "))
    attempts += 1
    if guess == key:
        print(f"Yay! you guessed it correctly in {attempts} attempts")
        break
    elif guess < key:
        print("guess higher!")
    elif guess > key:
        print("guess lower!")