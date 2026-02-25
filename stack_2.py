import Node
import Stack
#starting to create our stack
stack1 = Stack.Stack()

s_size = int(input("Size of stack: "))

for i in range(1,s_size+1):
    i = input(f"enter element {i}:")
    stack1.push(i)
print("\nCurrent Stack:", end=" ")
stack1.printstack()

task = 0
while True:
    print(" ")
    print("1. Push element")
    print("2. Pop element")
    print("3. View top element")
    print("4. Print Stack")
    print("5. End program")

    task = input("Enter the task to perform: ")

    if task == "1":
        pushe = input(f"enter element to push:")
        stack1.push(pushe)
        print("\nNew Stack:", end=" ")
        stack1.printstack()

    elif task == "2":
        pope = stack1.pop()
        print("Popped:", pope)
        print("\nNew Stack:", end=" ")
        stack1.printstack()

    elif task == "3":
        viewe = print(f"Top element is: {stack1.peek()}" )

    elif task == "4":
        print("\nCurrent Stack:", end=" ")
        stack1.printstack()  

    elif task == "5":
        print("Stack implimentation done")
        break


