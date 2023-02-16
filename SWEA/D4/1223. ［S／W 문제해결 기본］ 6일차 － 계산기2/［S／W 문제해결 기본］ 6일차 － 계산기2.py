for test_case in range(1, 11):
    input()
    string = input()
    operator = ['+', '*', '(', ')']
    sequencing = ['+', '(', ')']
    lst = []
    stack = []
    for c in string:
        if c not in operator:
            lst.append(c)
        else:
            if c == ')':
                while stack[-1] != '(':
                    lst.append(stack.pop())
                else:
                    stack.pop()
            elif c == '+' and (not stack or stack[-1] == '*'):
                while len(stack) > 0 and stack[-1] == '*':
                    lst.append(stack.pop())
                stack.append(c)
            else:
                stack.append(c)
    else:
        while stack:
            lst.append(stack.pop())

    answer = int()
    stack = list()
    for c in lst:
        if c not in operator:
            stack.append(c)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            if c == '+':
                stack.append(left+right)
            elif c == '*':
                stack.append(left*right)
    else:
        answer = stack.pop()
    print(f'#{test_case}', answer)
