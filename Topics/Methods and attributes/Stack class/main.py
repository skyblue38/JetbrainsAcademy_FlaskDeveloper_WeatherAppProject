class Stack:

    def __init__(self):
        self.stack_list = []
        self.stack_depth = 0

    def push(self, el):
        self.stack_list.append(el)
        self.stack_depth += 1

    def pop(self):
        if self.stack_depth > 0:
            self.stack_depth -= 1
            return self.stack_list.pop()
        return None

    def peek(self):
        return self.stack_list[-1]

    def is_empty(self):
        return self.stack_depth == 0
