def is_possible(x, y, direction):
    dx, dy = direction
    if (dx, dy) == (0, 0):
        return True
    while 0 <= x+dx < N and 0 <= y+dy < N:
        x, y = x+dx, y+dy
        if board[x][y] == 1 or connected[x][y]:
            return False
    return True


def connect(x, y, direction, length):
    dx, dy = direction
    if (dx, dy) == (0, 0):
        return length
    while 0 <= x+dx < N and 0 <= y+dy < N:
        x, y = x+dx, y+dy
        connected[x][y] = True
        length += 1
    return length


def disconnect(x, y, direction, length):
    dx, dy = direction
    if (dx, dy) == (0, 0):
        return length
    while 0 <= x+dx < N and 0 <= y+dy < N:
        x, y = x+dx, y+dy
        connected[x][y] = False
        length -= 1
    return length


def dfs(cnt, connected_cnt, length):
    global max_connected_cnt, min_length
    if cnt == len(cores):
        if connected_cnt > max_connected_cnt:
            max_connected_cnt = connected_cnt
            min_length = length
        elif connected_cnt == max_connected_cnt:
            min_length = min(min_length, length)
        return

    x, y = cores[cnt]
    for direction in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
        if is_possible(x, y, direction):
            if direction == (0,0):
                add = 0
            else:
                add = 1
            new_length = connect(x, y, direction, length)
            dfs(cnt+1, connected_cnt+add, new_length)
            length = disconnect(x, y, direction, new_length)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = [(i, j) for i in range(1, N-1) for j in range(1, N-1) if board[i][j] == 1]
    connected = [[False]*N for _ in range(N)]
    max_connected_cnt, min_length = 0, N*N
    dfs(0, 0, 0)
    if min_length == N*N:
        min_length = 0
    print(f"#{test_case} {min_length}")