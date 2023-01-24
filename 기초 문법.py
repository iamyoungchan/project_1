b ='  Hi SIRI  '
b.lower() # 소문자로 변환
b.replace("H", "i") # replace("바뀌게 될 문자열", "바꿀 문자열")
b.split() # 괄호 안 변수 기준으로 문자열 분리
sorted(b) # 정렬해서 리스트로 반환 (스트링도 가능)
b.strip() # 양쪽 공백 삭제 (rstrip, lstrip은 각각 왼쪽, 오른쪽 공백 삭제)
b.count('H') # H 몇 개인지
b.index('H') # H 몇 번째에 있는지

# 리스트
c = ['hi', 8, ['a', 'b', 'c']]
del c[0] # = c.remove(3)
c.append(53) # 리스트에 53 추가
c.reverse() # 역순 정렬 (그냥 순서만 뒤집는거)
c.insert(n번째 위치, 문자) # n번째 위치에 삽입

a = 'hello'
list(a) # 문자열은 리스트로 바꾸면 한 글자씩 쪼개져서 넣어짐

# 리스트 복사 주의
c2 = (1,2,3)
c3 = c2
c2[0] = 1 # 이때 c3와 c2는 동일한 주소의 리스트를 공유하기에 같이 바뀜
c4 = c2[:] # 공유하지 않게 복사해서 삽입

# 튜플 (리스트와 유사하지만 값 수정 불가능해서 잘 안 씀)
d = (1, 2, 3)

# 딕셔너리 (인덱싱 불가)
e = {'name' : 'PYC', 'birth' : '020504', 1 : [1,2,3]}
e['phone'] = '01039284206' # 쌍 추가

e.get('number','없습니다') # e에 number라는 키 값이 없으면 '없습니다'를 반환
e.keys() # 딕셔너리의 키 값을 모아주는 것 list(e.keys())하면 리스트로 형 변환 가능, e.values()도 동일하게 가능
del e['name'] # key값이 name인 쌍 삭제
e.clear() # 모든 요소 삭제

# 집합(set) (딕셔너리에서 value값만 쓴 것과 동일하며 중복값은 자동 삭제, 인덱싱 불가)
f = set([1,2,3,4,4,4])
f2 = {1, 3, 6, 6}

f & f2 # 교집합
f | f2 # 합집합
f - f2 # 차집합
f.add(5) # f 집합에 5 추가 # 여러 값이면 update

# if문
# pass 입력시 탈출 / else if는 elif로 쓰기

# while문 (for문과 달리 자동 +1 없으므로 주의)
while score < 100:
    score = score + 1
    print(f'점수는 {score}이다.')

money = 1000
while money: # 무한루프 (0이 아닌 숫자는 모두 True, money는 0이 아니므로 True임)
    break 

# for문
i = [(1,2), (3,4), [5,6]] 
for (a, b) in i: # a,b 값이 (1,2) -> (3,4) -> (5,6)

i_2 = '123'
for i in i_2: # i는 차례대로 '1', '2', '3'이 됨

# 함수 
def k(choice, *l): # 여러 개의 변수를 입력 받을 때에는 * 붙이기, **이면 딕셔너리 입력 받기(키 값에 따옴표 X)
    if (choice == 'ok'):
        result = 0
        for i in l:
            result = result + 1
    return result
k('ok', 1,3,4,5)

def calc(x, y, opt='+'): # 함수 디폴트 값을 미리 넣어놓으면 입력값 없을 시 디폴트 값으로 실행
    if (opt == '+'):
        result = x+y
    return result

# join 함수 (튜플, 리스트 딕셔너리(키값) 모두 가능)
a = ['1', '2']
''.join(a) # 공백 없이 a의 요소를 합치기

# 문자열 구성 파악 함수
e = '12345'
e.isalpha() # 문자열 e가 알파벳으로만 구성되어 있다면 True 반환
e.isdigit() # 문자열 e가 숫자으로만 구성되어 있다면 True 반환

# 절댓값 함수
abs(-3)
