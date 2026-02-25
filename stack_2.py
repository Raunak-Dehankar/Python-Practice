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