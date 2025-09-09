# print("Hello, Python !")
#
# # 주석(comment) - 한 줄 주석 / 파이썬 인터프리터가 코드로 인식하지 않음
#
# # 사후 주석 -> ctrl + /
#
# '''
# 다중 주석 처리
# '''
# print(1)            # 숫자 자료형
# print('1')          # 문자열 자료형
#
# print(1+2)          # 결과값: 3
# print('1'+'2')      # 결과값: 12
#
# print(type('1'))    # 결과값 : <class 'str'>
# print(type(1))      # 결과값 : <class 'int'>
# print(type(1.1))    # 결과값 : <class 'float'>
#
# '''
# print() : 콘솔에 출력하는 '함수'
# type() : 소괄호 내에 있는 데이터(argument)가 어떤 자료형인지 알려주는 명령어
#     - JS에서는 typeof가 함수가 아니라 연산자였습니다.
# '''
# print('python 수업을 시작했습니다. 파이팅')
# print('''
# 이렇게 다중으로 작성하고 싶을 때는 \'\'\'\'\'\'으로 작성하는 방법도 있습니다.
# Java에서는 줄 넘어갈 때마다 +로 연결해줘야 했는데 그런 점은 편합니다.
# ''')
#
# '''
# 이상에서 알 수 있는 점은 print()가 System.out.println()처럼 자동 개행이 된다는 점입니다.
#
# 변수(Variable) : 데이터를 저장하는 바구니
# '''
# # 변수 선언 및 초기화
# # 변수명 = 데이터
# name = '김일'
# age= 20
# print('안녕하세요 제 이름은' + name + '입니다. 나이는 ' + str(age) + '살입니다.')
#
# '''
# python은 좀 까탈스러워서 Java나 JS할 때 처럼 맨 처음이 str이면 뒤의 int/float를 알아서 바꿔주는
# 짓을 안합니다.
#
# 그때 사용하는 형변환 함수(conversion)가 있는데
#
# str() : 다른 데이터를 문자열 자료형으로 바꿔주는 함수
# int() ; 문자열/실수 자료형을 정수형으로 바꿔주는 함수 / Java : (int)"1.3";
# float() : 실수 자료형으로 바꿔주는 함수
#
# 근데 귀찮다.
# 그래서 f-string 개념이 도입됐습니다.
# '''
# print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}살입니다.')
# '''
# 혹시 기억하신다면 JS에서 비슷한 개념을 배웠다는 것을 알 겁니다.
# console.log(`안녕하세요, 제 이름은 ${name}이고, 나이는 ${age}살입니다.`);의 python판이라고 생각하시면 됩니다.
#
# Java에서의 Scanner 같은 기능을 하는 함수 : input()
# '''
# name2 = input('이름을 입력하세요 >>> ')
# print(name2)

# tu = (1, 2, 3, 4, 1, 2, 3, 1, 2)
# print(tu, type(tu))
#
# print(tu.count(1)) # tu에서 1이라는 값이 몇 개 있는지 알려줘
# print(tu.index(1)) # tu에서 1이라는 값이 튜플의 몇번째 위치에 있는지 알려줘
#     # 중복된 값을 찾고자 하면 맨 앞에 있는 인덱스 번호만 알려줌

# set1 = {"사과", "참외", "파인애플", "멜론"}
# print(set1, type(set1)) #인덱스번호를 사용할 수 없는 비시퀀스 자료형
#
# # 세트의 메소드
# # .add()
# set1.add("포도")
# print(set1)  # set에 "포도"가 추가되어 있음
# set1.add("사과")
# print(set1) # set은 중복된 값을 가질 수 x
#
# # .remove(값)
# set1.remove("참외")
# print(set1) # 참외 삭제
#
# # .discard(값)
# set1.discard("포도")
# print(set1) # 포도 삭제
# set1.discard("수박") # 없는 값을 삭제하려고 해도 오류가 발생하지 x
#
# # pop()
# set1.pop()
# print(set1)

# 세트 생성
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# # 교집합
# # print(set1 & set2) # 2개의 세트의 공통 요소
# # inter_set = set1.intersection(set2)
# # print(inter_set)
# #
# # # 합집합
# # print(set1 | set2)
# # uion_set = set1.union(set2)
# # print(union_set)
#
# # 차집합
# print(set1 - set2)
# di_set = set1.difference(set2)
# print(di_set)
#
# #딕셔너리 생성
# di = {"A" : 1, "B" : 2}
# print(di, type(di))
#
# # 딕셔너리의 key로 value에 접근
# print(di["A"]) # 1
#
# # 딕셔너리의 요소 수정
# # 딕셔너리[key] = value(수정할 값)
# di["A"] = 10
# print(di)
#
# # 딕셔너리 메소드
# # .get(key)
# print(di.get("B")) # "B"의 value 2 변환
#
# # .pop(key)
# di.pop("B")
# print(di) # "B"와 해당하는 value값 2 삭제
#
# # 딕셔너리 요소 추가
# # 딕셔너리[key] = value
# # 기존에 없는 key를 작성
# di["C"] = 30
# print(di) # key는 C 해당하는 value 30 추가됨
#
# print(di.values())
#
# for i in di.values() :
#     print(i)
#
#     # .items()
#     print(di.items())
#
# for i in di.items() :
#     print(i, type(i)) # (key, value)
#
# for i in di.items() :
#     # 튜플의 언패킹 활용
#     key, value = i   # ("A", 10)
#     print(key, value)
#
# for key.value in di.items() :
#     print(key, value)

# 숫자 내장함수
# abs()
# print(abs(-10)) # -10의 절대값 -> 10
# print(abs(10)) # 10의 절대값 -> 10
#
# # divmod() : (몫, 나머지)
# print(divmod(10, 3), type(divmod(10, 3))) # (3, 1)
# print(10//3) # 3. 몫
# print(10 % 3) # 1. 나머지
#
# li = [1, 3, 5, 7, 9]
# print(max(li)) # li에서 가장 큰 값
# print(min(li)) # li에서 가장 작은 값
# print(sum(li)) # li의 요소들의 합

# pow()
# print(10 ** 2)
# print(pow(10, 2)) # 10 ** 2와 같다 (거듭제곱)
#
# # round()
# print(round(1.6)) # 2
# print(round(2.32)) # 2
# print(round(3.142, 2)) # 3.14, 소수점 2자리로 반올림
#
# # 시퀀스 내장함수
# # enumerate() : 리스트와 함께 사용. ( idx, 요소)
# li = ["A", "B", "C"]
#
# for i in enumerate(li) :
#     print(i, type(i)) # (idx, 값)
#
# for idx, element in enumerate(li) : # 튜플의 언패킹
#     print(idx, element)
#
# # len()
# str1 = "hello"
# li1 = [1, 2, 3, 4]
# di1 = {"a" : 1, "b" : 2}
# print(len(str1)) # 5
# print(len(li1)) # 4
# print(len(di1)) # 2 딕셔너리는 key, value가 항상 한쌍의 1개의 값이기 때문에
#
# # sorted()
# li2 = [5, 2, 7, 1, 8, 2, 3]
# print(sorted(li2)) # 오름차순 결과
#
# print(sorted(li2, reverse = True)) #내림차순 결과
#
# # zip()
# alpha = ["A", "B", "C", "D", "E"] #zip()함수를 사용하면 길이가 짧은 반복가능객체가 기준이 됨
# nums = [1, 2, 3, 4]
#
# # for문과 zip() 사용
# for i in zip(alpha, nums) :
#     print(i, type(i)) # 두 반복 가능 객체의 인덱스 번호가 일치하는 요소들끼리 묶어서 반환

# count()
# str1 = "best of best"
# print(str1, type(str1))
# print(str1.count("best")) # 2 str1에서 "best가 몇 번 나오는지 알려줘
#
# # find()
# str1 = "best of best"
# print(str1.find("best")) # str1에서 'best'가 처음 나온 위치 인덱스 번호 반환
# print(str1.find("worst")) # 찾는 문자열이 없을 경우 -1 반환
#
# # index()
# print(str1.index('best')) #0. find()와 기능이 같음
# # print(str1.index("worst")) # 없는 문자열을 찾으려고 하면 오류 발생
#
# # join()
# li = ["h", "e", "l", "l", "o"]
# print(li, type(li))
# print("".join(li)) # 리스트의 요소들이 하나의 문자열로 합쳐짐
# print("-".join(li)) # 리스트의 요소 사이마다 '-' 문자열이 추가되어 합쳐짐
#
#
# di = {"a" : 10, "b" : 20}
# print(di, type(di))
# print("".join(di)) # 딕셔너리늨 키만 연결됨
#
# # split()
# data = "Hello World"
# print(data, type(data))
#
# print(data.split(), type(data.split())) #문자열을 공백 문자 기준으로 분리 후 리스트에 저장한 결과 반환
# print(data.split('o')) # 문자열을 'o'라는 문자열로 분리
#
# # replace()
# data = "Life is too short"
# print(data)
# print(data.replace("short", "long")) # data라는 문자열에서 short를 long으로 바꿔줘
#
# # 불필요한 문자열 제거 메소드
# str1 = "*****1**2**3*****"
#
# print(str1.strip("*")) # 양쪽 끝에 있는 "*"을 제거
# print(str1.lstrip("*")) # 왼쪽 끝에 있는 "*"를 제거
# print(str1.rstrip("*")) # 오른쪽 끝에 있는 "*"을 제거

# 변수의 종류 1)지역변수 2)전역변수
# global_value = 100 # 전역변수
#
# def print_value(num) : # 매개변수도 일종의 지역변수
#     print(global_value) # 전역변수는 함수 내부에서도 사용 가능
#     local_value = 200 # 지역변수
#     print(local_value)
#     print(num)
#
# print(global_value)
#
# # 함수 호출
# print_value(20)
# # print(local_value) # 지역변수는 함수 밖에서 사용 불가
# # print(num) # 매개변수도 함수 밖에서 사용 불가
#
# ### 1) random 모듈
# import random
#
# # randint()
# print(random.randint(1, 10)) # 1~10 중 랜덤한 정수 반환
# # .(~의 ,~안에) : random.randint() => random 모듈 안의 randint()
#
# # randrange()
# print(random.randrange(10))  # 0 ~ 9
# print(random.randrange(2,10)) # 2 ~ 9
# print(random.randrange(2, 10, 3)) # 2 ~ 9 간격은 3인 정수 중 랜덤한 정수 반환 : 2 5 8
# # choice()
# li = ["a", "b", "c"]
# print(random.choice(li))
#
# # sample
# print(random.sample(li, 2))
#
# # 모듈에서 특정한 함수만 가져오기
# from random import randint, randrange
#
# print(randint(1, 5)) # 특정 함수나 import 할 경우 모듈명 작성하지 않아도 됨
# print(choice([1, 2, 3]))
# print(randrange(1, 10))
#
# import time
# # sleep()
# print("안녕하세요")
# time.sleep(3) #3초 딜레이
# print("안녕히계세요")
#
# # time()
# print(time.time())

import matplotlib.pyplot as plt # 별칭

# matplotlib : 데이터 분석 시 시각화할 때 사용
# .plot(x, y) : x축 데이터, y축 데이터를 설정하여 꺾은선 그래프를 작성

plt.plot([1,2,3,4], ["a","b","c","d"])
plt.show() # 그래프 출력



