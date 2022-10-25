name = input("Please enter your name: ")
age = int(input("How old are you, {0} ? " .format(name))) #dc sa folosesc int daca pot doar cu input ?
print(age)

# if age >= 18:
#     print("You are allowed to vote")
#     print("Put an X in the box")
#if age < 18:
#   print("You are not allowed to vote")
#   print("Please comeback in {0} years".format(18 - age))
# else:
#     print("Please comeback in {0} years" .format(18 - age))


if age < 18:
    print("Please comeback in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda")
else:
    print("You are allowed to vote")
    print("Put an X in the box")



