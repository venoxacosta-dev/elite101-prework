print("Hello! Welcome to the Elite 101 Launch Console.")

name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

print("\nMenu:")
print("1. About Elite 101")
print("2. Preview tickets")
print("3. Definition of Done")
print("4. Products")

choice = input("Choose an option (1-4): ")

if choice == "1":
  print("Elite 101 is a startup-style course where we build and ship software.")
elif choice == "2":
  print("Tickets are small tasks with a clear finish line.")
elif choice == "3":
  print("Definition of Done means the work meets the requirements and is ready to ship.")
elif choice == "4":
  print("Our startup can build products that solve useful problems.")
else:
  print("That's not a valid option.")

print(f"\nThanks for using the Launch Console, {name}!")
