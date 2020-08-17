import sys
sys.setrecursionlimit(10000) #안 쓰면 효율성 검사에서 틀림

def find_empty_room(num, room_dic):
    if num not in room_dic:    #num 에 배정 가능
        room_dic[num] = num+1  #다음 num을 찾는 고객은 num+1번 방을 체크 
        return num
    else:
        new = find_empty_room(room_dic[num], room_dic)
        room_dic[num] = new+1
        return new
        

def solution(k, room_number):
    dic = {}
    ans = []
    for n in room_number:
        a = find_empty_room(n, dic)
        ans.append(a)
    return ans