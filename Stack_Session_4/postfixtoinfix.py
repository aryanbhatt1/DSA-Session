class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.array = []

        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "Overflow!"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def postfixToInfix(self, exp):
        for i in range(0, self.capacity):
            c = exp[i]
            if (c == '*' or c == '/' or c == '^' or c == '+' or c == '-'):
                var1 = self.pop()
                var2 = self.pop()
                temp = "(" + var2 + c + var1 + ")"
                self.push(temp)
            else:
                self.push(c + "")
        result = self.pop()
        print(result)


if __name__ == '__main__':
    exp = input("Enter expression")
    obj = Conversion(len(exp))
    obj.postfixToInfix(exp)
