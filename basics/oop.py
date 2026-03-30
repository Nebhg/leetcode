class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack
    
    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return ("Stack: " + str(self.stack))

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(len(s))    # should print 3
    print(s)         # calls __str__
    print(repr(s))   # calls __repr__