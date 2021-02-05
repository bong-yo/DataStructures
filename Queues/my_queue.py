class Queue:
    def __init__(self, initial_elements=[]):
        self.queue_elements = []
        for elem in initial_elements:
            self.enqueue(elem)

    def enqueue(self, element):
        self.queue_elements.append(element)

    def dequeue(self):
        if self.queue_empty():
            return False
        return self.queue_elements.pop(0)

    def remove(self, element):
        self.queue_elements = [x for x in self.queue_elements if x != element]

    def peek(self):
        if self.queue_empty():
            return False
        return self.queue_elements[0]

    def queue_empty(self):
        return not self.queue_elements

    def __len__(self):
        return len(self.queue_elements)

    def __str__(self):
        return str(self.queue_elements)


if __name__ == "__main__":
    q = Queue()
    print(q)
    x = q.dequeue()
    print(q)
    q.enqueue(3)
    print(q)
    q.enqueue(6)
    print(q)
    q.enqueue(2)
    print(q)
    x = q.dequeue()
    print(q)
