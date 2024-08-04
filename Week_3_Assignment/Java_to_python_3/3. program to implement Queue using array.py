class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

# User interaction
q = Queue()
while True:
    operation = input("Enter 'enqueue', 'dequeue', or 'exit': ").strip().lower()
    if operation == 'enqueue':
        item = int(input("Enter an item to enqueue: "))
        q.enqueue(item)
    elif operation == 'dequeue':
        try:
            print(f"Dequeued: {q.dequeue()}")
        except IndexError as e:
            print(e)
    elif operation == 'exit':
        break
    else:
        print("Invalid operation.")
