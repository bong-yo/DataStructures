class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elem):
        '''Add element on top of the stack'''
        self.elements.append(elem)

    def pop(self):
        '''Pop element on top of the stack'''
        return self.elements.pop(-1)

    def peek(self):
        '''Peek element on top of the stack'''
        return self.elements[-1]

    def __len__(self):
        return len(self.elements)


if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    print(stack.elements)
    stack.push(4)
    print(stack.elements)
    stack.pop()
    print(stack.elements)
    print(len(stack))
