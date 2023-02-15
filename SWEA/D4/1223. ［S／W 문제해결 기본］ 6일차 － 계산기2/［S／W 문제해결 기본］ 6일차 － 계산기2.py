for test_case in range(1, 11):
    size = input()  # not used
    operator = ['+', '*']
    answer = []
    stack = []
    for c in input():
        if c not in operator:
            answer.append(int(c))
        else:
            if c == '+':
                while stack:
                    answer.append(stack.pop())
                answer.append(c)
            if c == '*':
                stack.append(c)
    while stack:
        answer.append(stack.pop())
    for i in answer:
        if i == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
        elif i == '+':
            pass
        else:
            stack.append(i)
    else:
        answer = int(sum(stack))

    print(f'#{test_case}', answer)
