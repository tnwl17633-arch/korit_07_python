'''
아까 전에는 일종의 setter를 활용하여 속성에 속성값을 넣어줬음
그럼 Java에서 수업한 것처럼 속성값이 대입되지 않은 객체를 생성한 다음에 속성값을 집어넣어주는 과정을 거쳐야 함
근데 매개변수 생성자를 정의해버리면 객체 생성시에 속성값을 넣을 수 있겠네요.
'''
# 클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# # 객체 생성 ( 빈 객체 -> 속성값 대입 -> 속성값 출력)
# satang = Candy()
# satang.set_info('구형', '갈색')
# satang.show_info()
# '''
# 이게 굳이 속성값에 대한 제한이 있지 않다면 빈 객체 만들어놓고 거기에 값 대입하는 게 비효율적으로 느껴짐.
# 그래서 저희는 생성자를 도입할 것임.
#
# Java / JS 등에서는 생성자 명은 클래스명과 동일하거나 constructor인데, 또 python만 지 혼자서 이상한걸로 생성자를 만듦
# '''
# class Candy2():
#     # 생성자 정의
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# # 객체 생성 방식에서의 차이가 있습니다.
# satang2 = Candy2('정육면체', '흰색')
# satang2.show_info()
#
# class Sample:
#     #생성자 정의
#     def __init__(self):
#         print('인스턴스가 생성되었습니다.')
#
#     #소멸자 정의
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# # 객체 생성
# sample = Sample()
# print()
# # 객체 소멸자 호출 방법
# del sample        # del 객체명
# print('객체 지운 후의 코드라인입니다.')
'''
굳이 소멸자를 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지해서, 객체가 호출될 때마다 그곳에서 불려나오게 됩니다.

하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에 소멸자를 통해서
강제로 객체를 삭제해주면 메모리 관리가 편하겠네요.

그럴 때 씁니다. -> 저희 프로젝트 때는 뭐 굳이 안 쓸 것 같습니다.

기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
646B USB
'''

# class USB:
#     def __init__(self, capacity):
#         print('USB 객체가 생성되었습니다.')
#         self.capacity = capacity
#
#     def get_info(self):
#         print(f'{self.capacity}GB USB')
#
# usb = USB(64)
# usb.get_info()
#
# '''
# 응용 예제
#
# 1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.
#
# 지시 사항
# 1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오
# man = Person('james')
# woman = Person('emily')
# 2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
# james is born.
# emily is born.
#
# 3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
# del man
#
# 4. 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
# james is dead.
# '''
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} is born.')
# # 소멸자 정의하시오.
#     def __del__(self):
#         print(f'{self.name} is dead.')
#
#
# man = Person('james')
# woman = Person('emily')
#
# del man
# '''
# james is born.
# emily is born.  
# james is dead.
# emily is dead.
# 라고 결과값이 나옵니다. 이 이유는 모든 코드블럭이 다 읽어지면 메모리에 할당된 객체는 자동소멸하기 때문
# 그래서 강제로 emily is dead.를 출력하고 싶지 않다면 꼼수가 좀 필요
# '''
# # input('소멸자가 호출되는 것을 막는 중입니다.')
#
# '''
# python 판 getter / setter
# setter는 call2() -> 매개변수 o / 리턴 x
# getter는 call3() -> 매개변수 x / 리턴 o
# '''

# class Student:
#     # setter 예시
#     def set_name(self, name):
#         self.name = name
#
#     # getter 예시
#     def get_name(self):
#         return self.name

'''
지시 사항 
1. age / address / score 속성을 setter를 통해서 추가하시오.
2. 이상의 속성에 맞는 getter도 추가하시오.

student1 객체를 생성하고,
김일, 20, 4.5를 각각 이름/나이/점수에 대입하시오.

getter만을 활용하여, 
김일 학생의 나이는 20살로, 파이썬 과목의 점수는 4.5점입니다. 라고 출력하시오.

그렇다면 Java를 기준으로 봤을 때 setter 내부에는 비지니스 로직이 들어갈 수 있었습니다.

완전 동일하게 할겁니다.

set_age()의 경우에 내부에 로직으로 0살 미만과 200살 초과의 나이는 입력이 불가능하게끔 하겠습니다.

set_score()의 경우에도 0.0 미만과 4.5 초과는 입력이 불가능하게끔 비지니스 로직을 작성하세요.

여기서 생기는 의문점은 그겁니다 -> 아니 매개변수 생성자를 통해서 생성했는데 객체 생성 시점에 -102살 입력하면 되는거 아니냐 할 수 있는데
추후 설명하겠습니다.


'''
class Student:
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        # 0 미만 200 초과 입력 불가능 하게
        if age < 0 or age > 200:
            print('불가능한 나이 입력입니다.')
            return          # 메서드에 return 하고 비워두면 메서드 종료라는 의미
        self.age = age

        print('입력이 불가능합니다.')
    def set_score(self, score):
        if score < 0 or score > 4.5:
            print('불가능한 점수 입력입니다.')
            return
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score

print()
student1 = Student()
student1.set_name('김일')
student1.set_age(20)
student1.set_score(4.5)

print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()} 살로, 파이썬 과목의 점수는 {student1.get_score()}점입니다.')

if age >= 19:
    # 중첩 if문 적용
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요')
else:
    print('미성년자는 출입할 수 없습니다.')

age = float(age)        # 정수를 실수로 형변환
print(age)      # 결과값 : 21.0








