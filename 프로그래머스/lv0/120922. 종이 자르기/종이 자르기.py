def solution(M, N):
    if M == 1 or N == 1:
        return max(M, N)-1
    elif M <= N:
        return solution(M-1, N) + solution(1, N) + 1
    else:
        return solution(M, N-1) + solution(M, 1) + 1
