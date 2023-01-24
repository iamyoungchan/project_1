# n의 제곱근이 있다면 1, 없다면 -1 반환하는 함수 
def solution(n):
    temp = n**(1/2)
    if (temp % 1 == 0): 
        answer = 1
    else:
        answer = -1
    return answer

# int 12345 입력시 [5,4,3,2,1]을 출력하는 함수
def solution1(n):
    arr = []
    a = str(n) # 정수를 리스트에 하나씩 넣어줘야 하므로 스트링으로 바꿔서 for문 돌려주기 (for문은 숫자 하나로 안 돌아가니까)
    for i in a: 
        arr.append(int(i))
    arr.reverse()
    return arr
solution1(12345)

# int 12345 입력 시 내림차순으로 정렬하기
def solution(n):
    ls = list(str(n)) # 숫자를 스트링으로 바꿔서 리스트로 바꾸면 문자열 하나씩 쪼개서 넣어짐
    ls.sort()
    ls.reverse()
    return int("".join(ls)) # 간격 없이 리스트 요소 합치기

# 키패드 손가락 컨트롤
def solution(numbers, hand):
    left_hand = [1, 4, 7]
    right_hand = [3, 6, 9]
    answer = []
    left_location = 0
    right_location = 0
    for i in numbers:
        if (i in left_hand):
            answer.append("L")
            left_location = i
        elif (i in right_hand):
            answer.append("R")
            right_location = i
        else:
            left_ditance = abs(i - left_location)
            right_ditance = abs(i - right_location)
            if (left_ditance > right_ditance):
                answer.append("R")
                right_location = i
            elif (left_ditance < right_ditance):
                answer.append("L")
                left_location = i
            elif (left_ditance == right_ditance):
                if (hand == 'right'):
                    answer.append("R")
                    right_location = i
                elif (hand == 'left'):
                    answer.append("L")
                    right_location = i
    return ''.join(answer)
solution([1, 3, 4, 5, 8, 2, 1, 4, 5], 'right')
LRLLLRLLRRL
LRLLLRLLLRL