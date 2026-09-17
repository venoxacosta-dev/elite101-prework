print("Welcome to the Launch Console!")

name = input("What's your name? ")
print(f"Hi, {name}!")

running = True

while running:
    print("\nMenu:")
    print("1) About me")
    print("2) My goals")
    print("3) Fun fact")
    print("4) Exit")

    choice = input("Pick 1-4: ")

    if choice == "1":
        print(f"My name is {name}. I am learning to build software.")
    elif choice == "2":
        print("My goal is to improve my coding skills not just on Python but also with other coding languages.")
    elif choice == "3":
        print("Fun fact: I like sports and my favorite color is Royal blue.")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")