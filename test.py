while not stack1.isEmpty():
    print("\nCurrent Stack:", end=" ")
    stack1.printstack()

    user_input = input("Do you want to pop an element? (yes/no) ")
    if user_input == "yes":
        print("Popped:", stack1.pop())
    else:
        print("Stack implimentation done")
        break

if stack1.isEmpty():
    print("\nStack is empty.")