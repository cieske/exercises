def solution(A):
    sort = sorted(A)
    
    num_check = 1
    for i in range(len(sort)-1):
        if sort[i] == sort[i+1]:
            num_check += 1
        else:
            if num_check % 2 == 1:
                return sort[i]
            else:
                num_check = 1
                
    if num_check % 2 == 1:
        return sort[i]