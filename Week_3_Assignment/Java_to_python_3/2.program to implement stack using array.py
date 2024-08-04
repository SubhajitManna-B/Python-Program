class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

# User interaction
s = Stack()
while True:
    operation = input("Enter 'push', 'pop', 'peek', or 'exit': ").strip().lower()
    if operation == 'push':
        item = int(input("Enter an item to push: "))
        s.push(item)
    elif operation == 'pop':
        try:
            print(f"Popped: {s.pop()}")
        except IndexError as e:
            print(e)
    elif operation == 'peek':
        try:
            print(f"Top item: {s.peek()}")
        except IndexError as e:
            print(e)
    elif operation == 'exit':
        break
    else:
        print("Invalid operation.")
