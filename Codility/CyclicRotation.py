def solution(A, K):
    num = len(A)
    if num != 0: #Empty list check
        return A[-(K%num):] + A[:-(K%num)] #num < K check
    else:
        return A