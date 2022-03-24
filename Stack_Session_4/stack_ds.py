'''
Stack: Implementation as a list
'''


def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False


def Push(stk, item):
    stk.append(item)
    top = len(stack) - 1

def Pop(stk):
    if isEmpty(stack):
        return None
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item


def Peek(stk):
    if isEmpty(stk):
        return None
    else:
        top = len(stk) - 1
        return stk[top]


def Display(stk):
    if isEmpty(stk):
        print("Stack is Empty")
    else:
        top = len(stk) - 1
        print(stk[top], '<-top')
        for item in range(top - 1, -1, -1):
            print(stk[item])


if __name__ == "__main__":
    stack = []
    top = None

    while True:
        print(
            '''
            Stack Operations
            1. Push
            2. Pop
            3. Peek
            4. Display Stack
            5. Exit
            '''
        )

        choice = int(input('Enter Your Choice: '))

        if choice == 1:
            item = int(input('Enter item: '))
            Push(stack, item)
        elif choice == 2:
            item = Pop(stack)
            if item is None:
                print("Underflow! Stack is empty!")
            else:
                print("Popped item is {}".format(item))
        elif choice == 3:
            item = Peek(stack)
            if item is None:
                print("Underflow! Stack is empty!")
            else:
                print("Topmost item is", item)
        elif choice == 4:
            Display(stack)
        elif choice == 5:
            break;
        else:
            print("Invalid Choice!")
