grades = []
grade = {"name" : "홍길동", "KOR" : 80, "ENG" : 75, "MATH" : 55}
grades.append(grade)
grade = {"name" : "춘향이", "KOR" : 20, "ENG" : 55, "MATH" : 35}
grades.append(grade)

average_H = (grades[0]['KOR'] + grades[0]['ENG'] + grades[0]['MATH']) / 3
average_C = (grades[1]['KOR'] + grades[1]['ENG'] + grades[1]['MATH']) / 3

print(f'홍길동의 과목 평균은 {average_H}이고, 춘향이의 과목 평균은 {average_C}이다.')

# 2단 구구단 만들기 (while문)
i = 1
dan = 2

while i <= 9:
    result = dan * i
    print(f'{dan} * {i} = {result:2d}')
    i = i + 1

# 단 입력받아 구구단 출력 (while문)
dan = input("단수를 입력하세요 : ") # input은 스트링으로 입력받음
dan = int(dan) # 숫자로 타입 변환해주기 (타입 캐스팅)

while i <= 9:
    result = dan * i
    print(f'{dan} * {i} = {result:2d}')
    i = i + 1

# 구구단 출력 (for문)
for dan in range(1,10):
    print(f'구구단 {dan}단')
    for i in range(1,10):
        result = dan * i
        print(f'{dan} * {i} = {result:2d}')

# 리스트 예제
# 1. 리스트 평균 출력
grade_sum = 0
grade_list = [70, 60, 55, 75, 90, 80 ,85, 100]
for grade in grade_list:
    grade_sum = grade_sum + grade
    grade_average = grade_sum / len(grade_list)
print(f'성적의 평균은 {grade_sum / len(grade_list)}이다.')

# 2. 리스트 최댓값 출력
max = grade_list[0]
for grade in grade_list:
    if grade > max:
        max = grade
max

# 3. 리스트 평균과 가장 근접한 값 출력
grade_closer = abs(grade_list[0] - grade_average) # 일단 첫 번째 점수가 평균 근삿값이라고 가정
grade_closer_value = grade_list[0] # 첫 번째 점수와 평균의 차이값

for i in grade_list:
    temp_closer = abs(i - grade_average)        # for문 돌려서 다른 요소들의 차이 구하기
    if temp_closer < grade_closer_value:        # for문 돌아가다가 차이가 더 작은 값이 나오면     
        grade_closer_value = temp_closer        # 값 교체하기
        grade_closer = i        # 평균과 가까운 점수 출력이므로 프린트 할 최소 차이값에 해당하는 점수도 넣어주기
print(f'평균과 가장 근접한 점수는 {grade_closer}점이다.')

# 4. 리스트 요소들과 평균값의 차이 출력
grade_avg_diff = []
for grade in grade_list:
    grade_avg_diff.append(abs(grade - grade_average))
print(f'요소와 평균값의 차이는 {grade_avg_diff}이다.')

# 별 생성 예제
i = 0
while True:
    i = i + 1
    if (i > 5):
        break
    print(i*'*')

# 1~10까지 홀수만 출력
for i in range(11):
    if (i % 2 != 0):
        print(i)

# 점수 입력받아 학점으로 출력
grade = []

while True:
  score = int(input("점수를 입력하세요, 그만 입력하려면 0을 입력하세요 : "))
  if (score < 0 and score > 100):
    print("점수 입력이 잘못되었습니다. 다시 입력해주세요")
  elif (score == 0):
    print("점수 입력을 중지합니다.")
    break
  elif (score >= 90):
    grade.append('A')
  elif (score >= 80):
    grade.append('B')
  elif (score >= 70):
    grade.append('C')
  elif (score >= 60):
    grade.append('D')
  else:
    grade.append('F')
print(f'입력된 점수의 학점은 순서대로 {grade}입니다.')

# 1부터 1000까지 3의 배수의 합 (for문과 range함수 사용)
sum = 0
for i in range(1,1001):
  if (i % 3 == 0):
    sum = sum + i
print(f'1부터 1000까지 3의 배수의 합은 {sum}이다.')

# 팩토리얼 (자기 자신을 리턴하는 재귀함수를 이용)
def fac(n):
    if (n==1):
      return 1
    return n * fac(n-1)

def fac2(n):
  result = 1
  for i in range(n, 0, -1):
    result = result * i
  return result

# for문으로 list 요소 값 바꿀 때
a = [1,2,3,4,5]
for i in range(len(a)):
    a[i] = 10

#  연산자(+ 또는 *) 와 여러 정수를 입력받아 입력된 모든 수를 더하거나 곱한 결과를 
#  아래와 같은 형식으로 출력하는 프로그램을 함수를 사용해서 작성하시오.

# "계산식: 10 + 5 + 5 + 7"
# "결과값: 27

def calc(oprator, *x):
    temp = []
    if (oprator == '+'):
        result_value = 0
        for i in x:
            temp.append(str(i))
            result_value = result_value + i
        result = '+'.join(temp)

    elif (oprator == '*'):
        result_value = 1
        for i in x:
            temp.append(str(i))
            result_value = result_value * i
        result = '*'.join(temp)

    print(f'계산식 : {result}')
    print(f'결과값 : {result_value}')
    return

# 타이머 알고리즘
from math import radians
import time
def start_timer(cnt):
    while cnt > 0:
        print(f"{cnt//60}분 {cnt%60}초 남았습니다.")
        time.sleep(1)
        cnt = cnt - 1
    print("Time is up...")
    
    minutes = input("Minutes: ")
    seconds = input("Seconds: ")
    if not minutes.isnumeric() or not seconds.isnumeric():
        print("입력 에러")
        exit()
    cnt = int(minutes)*60 + int(seconds)
    try:
        start_timer(cnt)
    except:
        print("타이머가 중단되었습니다.")

start_timer(70)

import time
def start_timer2():
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))
    cnt = minutes*60 + seconds
    while cnt == 0:
        if (seconds == 0):
            if (minutes != 0):
                minutes = minutes - 1
                seconds = 60         
        print(f"{minutes}분 {seconds}초 남았습니다.")
        time.sleep(1)
        seconds = seconds - 1
        cnt = cnt - 1
        if (cnt == 0): print("timer stopped")

start_timer2()

# 로또 알고리즘
import random
def lotto():
    lotto_number = []
    while True:
        number = random.randint(1, 45)
        if number not in lotto_number:
            lotto_number.append(number)
        if (len(lotto_number) == 6): 
            break
    lotto_number.sort()
    lotto_number
    print("금주의 로또 번호")
    print("===============")
    for i in lotto_number:
        print(f"|{i}|")
        time.sleep(1)
    print("===============")
lotto()

# 슬롯머신 (1000원 지불하고 3개의 숫자를 뽑을 때 7 하나 당 3650원 얻는 게임)
import random
def game():
    global credit
    num_list = []
    for i in range(3):
        number = random.randint(0, 9)
        num_list.append(number)
    print(num_list)
    credit = credit - 1000
    if 7 in num_list:
        credit = credit + 3500
        print(f"당첨입니다. 현재 잔고는 {credit}원입니다.\n")
    else:
        print(f"꽝입니다. 현재 잔고는 {credit}원입니다.\n")

def Bet():
    global credit
    game()

def Deposit():
    global credit
    credit = int(input("금액을 입력하세요 : "))

def N_times_Bet():
    i = 1
    global credit
    N = int(input("횟수를 입력하세요 : "))
    while (i <= N):
        game()
        i = i + 1

def Auto_Bet():
    global credit
    i = 1
    import random
    number = random.randint(1, 100)
    print(f"{number}번 게임을 실행합니다.")
    while (i <= number):
        game()
        i = i + 1

def bet_machine():
    global credit
    credit = 0
    while True:
        print("1. Bet")
        print("2. Deposit")
        print("3. N-times Bet")
        print("4. Auto Bet")
        print("5. Quit")
        menu = input("메뉴의 번호를 입력하세요.")

        if (menu == '1'):
            if (credit < 1000):
                print("금액이 부족합니다. 더 충전하세요")
            else:
                Bet()
        elif (menu == '2'):
            Deposit()
        elif (menu == '3'):
            if (credit < 1000):
                print("금액이 부족합니다. 더 충전하세요")
            else:
                N_times_Bet()
        elif (menu == '4'):
            if (credit < 1000):
                print("금액이 부족합니다. 더 충전하세요")
            else:
                Auto_Bet()
        elif (menu == '5'):
            print("프로그램을 종료합니다.")
            break

bet_machine()

# 05-1 클래스(빵틀)와 객체(빵)
class Cookie:
    name = 'COOKIE'
    cost = 1200

cookie1 = Cookie()
print(cookie1.name, cookie1.cost)

class breads:
    def set(self, name):
        self.name = name
    def display(self):
        print(self.name)

bread1 = breads() # 객체 생성
bread1.set("소보루빵") 
bread1.name
bread1.display()

class Breads:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def display(self):
        print(self.cost, self.name)

bread1 = Breads("pizza_bread", 1400) # init 함수가 존재하므로 바로 변수 부여
bread1.display()

