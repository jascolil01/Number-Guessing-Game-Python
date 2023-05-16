import random

num = input('How large of a number would you like to guess up to? ')

if num.isdigit():
    num = int(num)

    if num <= 0:
        print('Please make the number larger than 0')
        quit()
else:
    print('Please make the input a number')
    quit()

r = random.randint(1, num)
guesses = 0

while True:
    guesses += 1
    user_guest = input("Make a guess of the number ")

    if user_guest.isdigit():
        user_guest = int(user_guest)
    else:
        print('Please make the input a number')
        continue

    if user_guest == r:
        print('Number is correct! great job!')
        break
    else:
        if user_guest > r:
            print("Your guess is over the number, try again")
        elif user_guest < r:
            print("Your guess is under the number, try again")

print(f"This took you {guesses} guesses to get {r}")
