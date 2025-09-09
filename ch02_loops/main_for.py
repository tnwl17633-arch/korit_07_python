'''
for 반복문
원래 python의 default for문의 경우 enhnaced for가 기본이기는 한데, 저희는 Java / JS 때 일반 반복문을 기준으로 한 것부터
학습했기 때문에 동일한 방식으로 나가겠습니다.

이때 좀 중요한게 rang()라는 함수
1
2
3
...
10
출력하는 for문 작성
'''
# for i in range(10):
#     print(i+1)
# '''
# 이상에서 중요한 것은 마찬가지로 i가 0부터 시작한다는 점입니다.
# 이를 Java / JS로 풀면
# for (int i = 0; i < 10; i++) {
#     System.out.println(i+1);
# }
# 이라고 할 수 있겠네요.
#
# range() : 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 함게 연계돼서 쓰이는 편
#
# range() 함수의 응용 :
#     range( (시작값), 종료값, (증감값) )
#
# 시작값 : 생략 가능, 생략하면 0부터 시작
# 종료값 : 명시하지 않으면 끝까지 진행
# 증감값 : 생략 가능, 생략할 경우에 1씩 증가
#
# for 반복문
# 형식 :
# for i(아무거나 사용가능) in range( 시작값, 종료값, 증감값):
#     반복실행문
# '''
# for i in range( 1, 10, 1 ):     # 중요한 점은 종료값 할 떄 '미만'으로 적용된다는 점입니다. Java 배웠으니까 이 부분은 별 문제가 인될 것
#     print(i)
# '''
# 전체 합쳐서 생각했을 때는 그러면 range() 내에 있는 부분이
# Java 상에서의 for()의 ()내에 있는 부분을 지정하는 것이라고 볼 수 있겠습니다.
# for ( int i = 1 ; i < 10 ; i++ )
# '''
# str_example = '안녕하세요'
# for i in str_example:
#     print(i)
# '''
# 근데 range()가 필수라는 것은 아니고, default 형태로 작성했을 떄의 형식은 다음과 같음
#
# 형식 :
# for 변수명  in iterable(반복가능객체):
#     반복실행문
#
# range() 함수를 쓸 필요 없이 반복 가능 객체(list / tuple / string / set 등)의 처음부터 끝까지 돌아갑니다. enhanced - for문과 유사하다고
# 할 수 있습니다. 추후 python collections 수업 후에 적극적으로 응용해서 작성하겠습니다.
# '''
#
# num_list = [ 1, 2, 3, 4, 5 ]
# for i in num_list:
#     print(i, end=' ')   #println이 아니라 한 줄에 쓰기 위해 사용하는 방식 : 추후 수업 예정
# print()
# print(6)
# # print() 함수는 자동 개행이기 때문에 마무리를 사용자화하고 싶다면 end= 키워드를 쓸 수 있습니다. 제 수업 떄는 별로 안 쓸 겁니다.

# for i in range (1, 10, 2):
#     print(i)
#
# for i in range(3): # 정수 0~2 3개
#     print("Hello~")
#
# for i in range(1,11) :
#     print(i)
#
#     if i == 5 :
#         print("프로그램 종료")
#         break # 반복문 강제 종료
#
# # 1~10까지 정수 중 5만 빼고 출력
# for i in range(1, 11):
#         if i == 5 :
#             continue
#         else :
#             print(i)
#             # pass문 : 조건문,반복문에 실행내용을 정하지 않았을 때 임시로 작성
#
# def add(x, y) : # 매개변수 :2개의 정수를 지정할 변수
#     # 함수의 기능 및 반환 값
#     result = x + y # 매개변수에 저장된 2개의 정수의 합 저장
#     return result # 두 정수의 합을 반환
#
# # 함수 호출(함수 사용)
# # 함수명(인수 ...)
# print(add(10,20)) # 인수 (10,20) : add()함수의 매개변수 x,y에 전달 => x, y에 저장된 값을 합한 30을 변환
# # print(add(10)) # 매개변수와 인수의 개수는 일치해야함
#
# # 반환값이 있는 함수는 값처럼 사용 => 변수 = 값
# result = add(30,40) # add()함수에 30, 40을 전달하여 반환 받은 값을 변수에 저장
# print(result)
#
# # 함수 정의(매개변수 , return 이 없는 경우)
# def say_hello() :
#     print("Hello~")
#
# # 함수 호출
# say_hello() #매개변수가 없으므로 전달할 인수 x
# say_hello()
# say_hello()
#
# def say():
#     print('j')
#
# say()
#
#
#
# def say_hello(name):
#     print("Hello~" + name)
#
# say_hello('허수지')

# def add_nums(num1, num2, num3, num4 = 40)  :
#     return num1 + num2 + num3 + num4
#
# print(add_nums(10, 20, 30))

# def show(*args) :
#     print(args, type(args))
#
# #함수 호출
# show(1, "python", 3)
# show("a", 3.14)

# str.count('a')
li1 = [10,20,30,40,50,60,70]
print(li1, type(li1))
print(li1[0], type[li1[0]])

li1[0] = 100 # li1의 0번 위치 값 100으로 수정
print(li1[0])
print(li1)

li1 = [1, 3, 5, 7, 9]
print(li1, type(li1))

li1.append(10)
print(li1)

li1.insert(1, 2)
print(li1)

li2 = [50, 70, 90]
li1.extend(li2)  # li1에 li2의 요소들 추가
print(li1)

# remove(값)
li1.remove(50) # li1에 있는 50을 삭제
print(li1)

# pop(idx)
li1.pop(0) # li1의 0번 위치의 값 삭제
print(li1)

li1.pop() # li1의 맨 끝의 요소 삭제
print(li1)

# 정렬
# .sort()
li = [1, 3, 2, 5, 2, 5, 4 , 6, 1]
print(li, type(li))

li.sort()
print(li) # 리스트 요소 오름차순 정렬

# .sort(reverse = True)
li.sort(reverse = True)
print(li) # 리스트 요소 내림차순 정렬

#.reverse()
li2 = ["a", 4, True, 3.3]
print(li2, type(li2))

li2.reverse()
print(li2) # 리스트 요소 역순 정렬

# .clear() : 리스트 요소 전체 삭제
li2.clear()
print(li2) # 빈 리스트
# +) in, not in 연산(컬렉션이나 반복가능 객체에서 사용) :  있니? 없니? True , False

li = ["봄", "여름", "가을", "겨울"]
print(li, type(li))
print("봄" in li) # "봄"이라는 값이 li에 있니?? => True
print("사자" not in li) # "사자"라는 값이 li에 없니?> => True

1 tu = (10, 20, 30, 10, 10, "a", "b", 50)
print(tu, type(tu))
# 튜플은 시퀀스 자료형(인덱싱, 슬라이싱)
print(tu[0], type(tu[0]))
print(tu[:4], type(tu[:4]))

# 튜플은 인덱스 번호를 사용하여 수정 불가!
tu[0] = 100
print(tu)
