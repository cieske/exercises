def solution(N):
    N = str(bin(N)[2:]).split('1') #bin(N)을 통해 변환된 수는 '0b'로 시작
    return max([len(x) for x in N][:-1]) #가장 마지막 split은 제외