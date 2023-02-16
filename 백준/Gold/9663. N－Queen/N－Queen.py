from collections import deque

n = int(input())
queue = deque([i] for i in range(n))
ref = range(n)
answer = 0

while queue:
    tmp = queue.pop()
    r = len(tmp)
    if r == n:
        answer += 1
        continue
    for val in ref:
        if val not in tmp:
            for row, column in enumerate(tmp):
                if val + r == row + column or val - r == column - row:
                    break
            else:
                queue.append(tmp+[val])
print(answer)