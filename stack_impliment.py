# stack using list (lifo principle used)

stack1 = []

# Push: Add elements to the top
stack1.append('hello')
stack1.append('Batata')

print(stack1)

# Pop: to remove the top element
stack1.append('remove this')
print(stack1)

val = stack1.pop()
print(f"Removed: {val}")

#stack using deque (uses linked list so faster and more efficient for big stack)

from collections import deque

stack2 = deque()

# Push: Add elements to the top
stack2.append('flower')
stack2.append('clock')

print(stack2)

# Pop: to remove the top element
stack2.append('remove this too')
print(stack2)

val2 = stack2.pop()
print(f"Removed: {val2}")
