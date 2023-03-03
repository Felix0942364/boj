def othello(r, c, t):
    array[r][c] = t
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]
    for i in range(8):
        ptr = 0
        for j in range(1, arr_size):
            if 0 <= r + j * dr[i] < arr_size and 0 <= c + j * dc[i] < arr_size:
                if array[r + j * dr[i]][c + j * dc[i]] and array[r + j * dr[i]][c + j * dc[i]] != t:
                    ptr += 1
                elif array[r + j * dr[i]][c + j * dc[i]] == t:
                    while ptr:
                        array[r + ptr * dr[i]][c + ptr * dc[i]] = t
                        ptr -= 1
                    break
                else:
                    break
            else:
                break


T = int(input())
for test_case in range(1, 1 + T):
    arr_size, moves = map(int, input().split())
    array = [[0] * arr_size for _ in range(arr_size)]

    # 흑돌
    array[arr_size // 2 - 1][arr_size // 2] = 1
    array[arr_size // 2][arr_size // 2 - 1] = 1
    # 백돌
    array[arr_size // 2][arr_size // 2] = 2
    array[arr_size // 2 - 1][arr_size // 2 - 1] = 2

    for _ in range(moves):
        column, row, color = map(int, input().split())
        othello(row - 1, column - 1, color)

    answer_black = 0
    answer_white = 0
    for row in array:
        answer_black += row.count(1)
        answer_white += row.count(2)

    print(f'#{test_case}', answer_black, answer_white)