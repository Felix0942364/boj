T = int(input())
for test_case in range(1, 1+T):
    change = int(input())
    ref = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = [0] * 8
    for idx, r in enumerate(ref):
        answer[idx] = change // r
        change %= r
    print(f'#{test_case}')
    print(" ".join(map(str, answer)))
