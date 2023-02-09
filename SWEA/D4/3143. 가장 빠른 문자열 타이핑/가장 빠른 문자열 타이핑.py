T = int(input())
for test_case in range(1, 1+T):
    hay_stack, needle = input().split()
    result = hay_stack.count(needle)
    result += len(hay_stack) - len(needle)*result
    print(f'#{test_case} {result}')