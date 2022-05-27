import random
number=random.randint(1,9)
guess=int(input("Enter your guess:"))
chances=5
print(guess)
guess2=str(guess)
number2=str(number)
while chances<=5:
    for guesses in guess2:
        if guess2<number2:
            print(input("Your guess was too low:Guess again"))
        elif guess2>number2:
            print(input("Your guess was too high: Guess a number lower than that"))
        elif guess2==number2:
            print("You're such a nerd damn..")
        elif not guess2 == number2:
            print("Lmao you loser XD")
