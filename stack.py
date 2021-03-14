class Stack:
    def __init__(self):
        self.s = []

    def top(self):
        if self.s:
            return self.s[-1]
        raise IndexError('Stack is empty')

    def pop(self):
        if self.s:
            return self.s.pop(len(self.s) - 1)
        raise IndexError('Stack is empty')

    get = pop

    def empty(self):
        return len(self.s) == 0

    def push(self, v):
        self.s.append(v)

    put = push

    def depth(self):
        return len(self.s)

    def back(self):
        self.s[:] = self.s[::-1]

    def __str__(self):
        return self.s.__str__()

    def __repr__(self):
        return self.s.__repr__()

    def __len__(self):
        return self.s.__len__()
