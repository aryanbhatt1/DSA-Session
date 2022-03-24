# Infix Evaluation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return "Stack is empty!"
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False

    def show(self):
        return self.stack


def applyOp(op, var2, var1):
    if op == '+':
        return int(var1) + int(var2)
    elif op == '-':
        return int(var1) - int(var2)
    elif op == '*':
        return int(var1) * int(var2)
    elif op == '/':
        if var2 == 0:
            return "infinity"
        else:
            return int(var1) / int(var2)
    else:
        return 0


def hasPrecedence(op1, op2):
    if op2 == '(' or op2 == ')':
        return False
    elif (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
        return False
    else:
        return True


expr = input("Enter the expression:")
tokens = map(str, expr)
tokens = ' '.join(tokens).split()


var = Stack()
ops = Stack()

skip = 0
for i in range(len(tokens)):
    if skip >= 1:
        skip -= 1
        continue
    if tokens[i] >= '0' and tokens[i] <= '9':
        num = tokens[i]

        for j in range(i + 1, len(tokens)):
            if tokens[j] >= '0' and tokens[j] <= '9':
                num = num + tokens[j]
                skip += 1
            else:
                break

        var.push(num)
        print(var.show())


    elif tokens[i] == '(':
        ops.push(tokens[i])

    elif tokens[i] == ')':

        while ops.peek() != '(':

            value = applyOp(ops.pop(), var.pop(), var.pop())
            if (value == "infinity"):
                print("Invalid Expression")
                break
            else:

                var.push(value)
        ops.pop()

    elif tokens[i] in ('+', '-', '*', '/'):
        while ops.isEmpty() is False and hasPrecedence(tokens[i], ops.peek()):
            x = applyOp(ops.pop(), var.pop(), var.pop())

            var.push(x)
        ops.push(tokens[i])

while (ops.isEmpty() is False):
    var.push(applyOp(ops.pop(), var.pop(), var.pop()))

print("Result of the expression is " + str(var.pop()))
