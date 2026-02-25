#this sets each element as node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    #this will define what our stack will be
    def __init__(self):
        self.head = None
        self.size = 0
    # empty stack is created 

    # now we will create a function to push an element in stack
    def push(self, value):
        # new stack node started 
        node_start = Node(value)
        #link the nodes and set the pushed one as head
        if self.head:
            node_start.next = self.head
        self.head = node_start
        self.size += 1

    # to pop or remove the topmost recently added node
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        # move the head pointer to the next value and reduce size 
        pop_node = self.head
        self.head = self.head.next
        self.size -= 1
        return pop_node.value
        
    # to check if the stack is empty 
    def isEmpty(self):
        return self.size == 0
    
    # to check the topmost value of stack
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.head.value
    
    # print the stack
    def printstack(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value, end=" -> ")
            currentnode = currentnode.next
        print()
    

#starting to create our stack
stack1 = Stack()

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


