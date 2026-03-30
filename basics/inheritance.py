from oop import Stack as stack

class MinStack(stack):
    def __init__(self):
        super().__init__()
        self.min_stack = []
    
    def push(self, val):
        super().push(val)
        # now decide whether val should go on min_stack
        # if min_stack is empty OR val <= top of min_stack:
        # push val onto min_stack
        # hint: what is the current minimum?
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        top = self.stack[-1]
        super().pop()
        # decide whether min_stack needs updating too
        if  top == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        # just peek at the top of min_stack
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    
if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.push(2)
    print(s.get_min())  # should be 2
    s.pop()
    print(s.get_min())  # should be 3
    s.pop()
    print(s.get_min())  # should be 3
    s.pop()
    print(s.get_min())  # should be 5