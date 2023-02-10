def solution(numbers):
    stack = []
    size = len(numbers)
    answer = [0] * size

    for i in range(size):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    while stack:
            answer[stack.pop()] = -1
    
    return answer
