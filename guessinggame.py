answer = 5

print("Print guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please enter a highter number")
elif guess > answer:
    print("Please enter a lower number")
else:
    print("You got it right")