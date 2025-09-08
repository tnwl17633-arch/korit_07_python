# li = [1, 1, 3.2, True, "a"] # 리스트 변수에 저장
# #       0   1  2   3     4  인덱스 번호
# print(li, type(li))
#
# # 리스트는 시퀀스 자료형 => 인덱스 번호를 사용
# # 1) 인덱싱
# print(li[0], type(li[0]))
# print(li[3], type(li[3]))
#
# print(li[1:4], type(li[1:4])) # idx 1~3까지 슬라이싱 (4는 미포함)
#
# ## 2) 튜플
# tu = (1, 1, 2, 3.3, True, "a") # 중복값 가질 수 있으며 모든 자료형 허용
# #     0  1  2   3    4     5
# print(tu)
# print(tu, type(tu))
#
# # 튜플은 시퀀스 자료형
# # 1) 인덱싱
# print(tu[1], type(tu[1]))
# #  2) 슬라이싱
# print(tu[:3], type(tu[:3])) # idx 0~2까지 슬라이싱, 타입은 튜플
#
# # +) 튜플의 요소가 1개일 경우
# tu2 = (2,) # 마지막에 ,(콤마) 작성
# print(tu2, type(tu2))
#
# # ** 튜플의 특징
# # 1) 패킹 :여러가지 값들을 ,(콤마)로 이어서 작성하면 튜플로 묶어줌
# tu3 = 1, 2, 3
# print(tu3, type(tu3))
# # 2) 언패킹 : 튜플의 각 요소들을 여러개의 변수에 할당
# num1, num2, num3 = tu3
# # num1, num2, num3 (1,2,3)
# print(num1, type(num1))
# print(num2, type(num2))
# print(num3, type(num3))
#
# set1 = {1,1,2,2,3}
# print(set1, type(set1)) # 세트는 중복값 허용x
# #세트는 비시퀀트 자료형 => 인덱스 번호 사용x
# # print(set1[0])
#
# # 딕셔너리
# # {key:value, key:value}
# di1 = {"A" : 1, "B" : 2}
# print(di1, type(di1))
#
# # value에는 여러 자료형 허용
# di2 = {"A반" : ["둘리", "도우너"], "B반" : "마이콜"}
# print(di2, type(di2))
#
#  # key로 value 접근 가능(key를 인덱스 번호처럼 사용)
#  # 변수명[인덱스번호]
#  # 딕셔너리명[key]
# print(di2["A반"], type(di2["A반"]))
# print(di2["B반"], type(di2["B반"]))
#
# # 비어있는 컬렉션 만들기
# # 1) 리스트 => [], list()를 이용하여 비어있는 리스트 생성
# li1 = []
# print(li1, type(li1))
#
# li2 = list()
# print(li2, type(li2))
#
# # 2) 튜플 -> (), tuple() 이용하여 비어있는 튜플 생성
# tu1 = ()
# print(tu1, type(tu1))
#
# tu2 = tuple()
# print(tu2, type(tu2))
#
# # 3) 세트 -> set() 함수 사용
# set1 = set()
# print(set1, type(set1))
#
# # 4) 딕셔너리 -> [], dict() 사용하여 비어있는 딕셔너리 생성
# di1 = []
# print(di1, type(di1))
#
# di2 = dict()
# print(di2, type(di2))
#
# # 제어문 (조건문) if 조건식 :
# #  (들여쓰기, tab) 조건식이 참일 떄 실행
#
# # <if문 예제>
# # 사용자가 입력한 정수가 100보다 크다면 "100보다 크다!"출력
#
# num = int(input("정수 입력 : ")) #점수를 입력받아 변수에 저장
#
# # 입력받은 정수가 100보다 크다면 "100보다 크다!" 출력
# if num > 100 :
#     # num > 100 -> True일 경우 실행
#     print("100보다 크다!")

# <if ~ else문 예제>
# 사용자로부터 정수를 입력받아 입력받은 정수가 짝수라면 "짝수"출력
# 그게 아니라면 "홀수" 출력

# 정수입력받기
# num = int(input("정수 입력 : "))

# num에 저장된 값이 짝수라면 "짝수" 그게 아니라면 "홀수" 출력
# if num % 2 == 0 :
#     # num이 짝수인 경우(짝수는 2로 나누면 나머지가 0)
#     print("짝수")
# else :
#     # num이 홀수인 경우(홀수는 2로 나누면 나머지가 1)
#     print("홀수")

# if ~ elif ~ else문
# 사용자로부터 정수를 입력받아 입력받은 정수가 20보다 크다면 "20보다 크다!"출력
# 그게 아니라 10이상이거나 20보다 작거나 같다면 "10이상 20이하입니다" 출력
# 그게 아니라 10 미만이거나 5보다 크거나 같다면 "10미만 5이상입니다"
# 그것도 아니라면 "5보다 작습니다" 출력

# num = int(input("정수 입력 :"))
#
# if num > 20 :
#     print("20보다 크다")
# elif num >= 10 :
#     print("10이상 20이하 입니다")
# elif num >= 5 :
#     print("10미만 5이상 입니다")
# else :
#     print("5보다 작습니다")
# while문 (반복문)
# 1~10까지 출력
# 1~10까지의 정수를 표현할 변수 생성
# num = 1
# while num <= 10 : # num에 저장된 값이 10보다 작거나 같을 동안 반복
#     # 반복할 문장 작성
#     print(num)
#     num += 1 # num에 저장된 값 1씩 증가

# for문  for 변수명 in 집합(컬렉션, 시퀀스자료형, range()....) :
# (들여쓰기, tab) 반복실행할 문장

# 문자열(시퀀스 자료형)과 for문





