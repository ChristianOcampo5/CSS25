# Christian Ocampo CSS-225 10/18/2024 team assignment lab

# Options 0-5 for users to select one of the given choices
choice = input("Please choose your option from the list below:\n"
               "{1. Learn Python}\n {2. Learn Java}\n {3. Go Swimming}\n {4. Have dinner}\n {5. Go to bed}\n {0. Exit}\n: ")
print(choice)

if choice.casefold() == '0':
    print("You chose 0")
elif choice.casefold() == '1':
    print ("you chose 1")
elif choice.casefold() == '2':
    print("you chose 2")
elif choice.casefold() == '3':
    print("you chose 3")
elif choice.casefold() == '4':
    print("you chose 4")
elif choice.casefold() == '5':
    print("you chose 5")
else:
    print("invalid choice!")