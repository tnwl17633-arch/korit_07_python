# from ctypes import pythonapi
#
# try :
#     a = int(input('나누는 수를 정수로 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 정수로 입력하세요 >>> '))
#     result = b / a          # 예외가 발생할 수 있는 구간이 try 문 내에 있어야만 합니다.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else :
#     print(f'b / a = {result}')
# finally:
#     print('프로그램이 종료되었습니다.')
# # ```
# # 결과적으로 개발자가 고려해야할 것은 일단 try를 써버리면 except안 썼을 떄 오류가 발생하기 때문에 try/except 문이 없는 상태에서 다양히게
# # 검증해보고 어떤 예외가 발생하는지 체크해야 합니다.
# # 그리고 그 발생한 예외들에 대한  except문을 작성해야 하고, 정상적으로 처리가 되었을 때 else문을 쓸 필요가 있을 겁니다.
# #
# # 하지만 이상의 사례와 같이 a = 0을 입력하는 것 자체가 예외를 발생시키지 않고,
# # 1. a = 0이면서,
# # 2. b / a 연산을 시도할 때 ZeroDivisionError가 발생하기 때문에,
# #
# # else문에 b/a가 포함되어서는 안됩니다.
# # 그래서 try문 내에 result = b / a 를 집어넣어줌으로써 그 부분이 예외 없이 통과되었을 때만 연산 결과가 출력될 수 있도록
# # `print(f'b / a = {result}')`로 정리했습니다.
# '''
# 이상의 상황에서 ZeroDivisionError 를 예외처리했음에도 불구하고
# a = 0
# b = 아무 정수
# 를 넣었을 때 ZeroDivisionError가 예외처리되지 않고 오류 발생을 하는 것을 확인할 수 있습니다. 어떻게 처리할지 고민하시오.
# '''
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f'{self.name}이(가) {food}를 먹습니다.')
#
#
# class Student(Person):
#
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#
#     def study(self):
#         print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')
#
#     def eat(self, food):
#         print(f'{self.school}에서', end= ' ')
#         super().eat(food)



# 객체 생성
# potter = Student('해리 포터', '호그와트')
# potter.eat('감자')
# potter.study()
# print('''
# '''
# 이상의 코드에서 주목해야 할 점은
# 1. Student 클래스에 정의되지 않은 메서드인 .eat()을 76 라인에서 호출했다는 점
# 2. Student 클래스의 생성자에서 확인되는 `super().__init__(name)`입니다.
#     - 해당 부분은 슈퍼 클래스의 생성자를 호출하는 방식입니다.
#     - Java에서는 슈퍼 클래스의 생성자 호출 방식이 super()
#     - Java에서 슈퍼 클래스의 메서드 호출 방식 super.메서드명()
# ```python
#     def eat(self, food):
#         print(f'{self.school}에서', end=' ')
#         super().eat(food)
# ```
# 만약에 이상과 같이 슈퍼 클래스의 메서드인 .eat()을 override하여 `재정의`하는 것도 가능합니다. Java와 달리 python에서는 기본적으로 `super().`을 베이스로 한다는 것을 알 수
# 있습니다.
# 생성자나 소멸자가 __가 앞뒤로 붙기는 하지만 기본적으로 method라는 사실을 알고 계신다면 Java보다 오히려 더 일괄적인 방식으로 코드를
# 작성한다는 점도 확인할 수 있겠습니다.

# class Person:
#     # 사람의 이름을 정의하는 메서드
#     def get_name(self, name):
#         self.name = name # self.데이터 속성 = 값
#         # Person 클래스의 name 데이터 속성에 매개변수 name에 저장된 인수 저장
#
#         # 사람의 나이를 정의하는 메서드
#     def get_age(self,age):
#         self.age = age
#
#         # 사람이 자신을 소개하는 메서드
#     def introduce(self):
#         print("내 이름은 ", self.name, "입니다.")
#         print("나이는 ", self.age, "살 입니다.")
#
#         # 클래스 사용 : 객체화
#         # 객체명 - 클래스명()
#
#         pr1 = Person() # Person의 pr1 객체 생성
#         # 속성 접근
#         # 1) 데이터 속성에 접근
#         pr1.name = "둘리" # pr1의 name데이터 속성에 "둘리" 저장
#         print(pr1.name)
#
#         # 2) 메서드 접근
#         pr1.get_age(10)  # pr1의 get_age()메서드 호출
#                           # pr1.age = age: 데이터 속성 age에 매개변수 age에 저장된 인수 저장
#         print(pr1.age)
#         pr1.introduce()
#
#         # 두 번째 객체 생성
#         pr2 = Person()
#         pr2.name = "도우너"    #pr2의 데이터 속성에 값 저장
#         age = 12
#         pr2.introduce()
#
#         # 생성자
#         # 생성자가 추가된 Person 클래스 선언
#         class Person :
#                 # 생성자 : name, age를 객체에 생성될 때 초기화
#             def __init__(self, name, age) :
#                 self.name = name
#                 self.age = age
#
#         #메서드
#             def introduce(self):
#                 print("제 이름은 ", self.name, "입니다")
#                 print("나이는", self.age, "살 입니다")
#
#         #객체화
# p1 = Person("둘리", 10) # 생성자는 객체를 생성할 때 실행
# p2 = Person("도우너", 11)
#
# p1.introduce()
# p2.introduce()
#
# class Student :
#     # 생성자 : 학생의 이름과 나이를 초기화
#     def __init__(self, name, age) :
#         self.name = name # 인스턴스 변수, 객체마다 다른 값을 저장하는 변수
#         self.age = age
#
# #Student 클래스 객체 생성
# st1 = Student("둘리", 12)
#
# print("=====데이터 속성=====")
#
# # 인스턴스 변수 호출 : 객체를 통해서만 접근 가능
# print(st1.name)
# print(st1.age)
#
# # 클래스 변수 호출 : 객체와 클래스를 통해 접근 가능
# print(st1.school_name)
# print(Student.school_name)
#
# print("=====메서드 호출=====")
#
# #인스턴스 메서드 호출 : 객체를 통해서만 호출
# st1.print_info()
# # 클래스 메서드 호출 : 객체와 클래스를 통해 호출 가능
# st1.print_school()
# Student.print_school()
#
#
# # 학생의 이름, 나이를 출력하는 메서드(인스턴스 메서드)
# def print_info(self) :
#     print("학생의 이름 : ", self.name)
#     print("학생의 나이 : ", self.age)
# # 학생들의 학교명을 출력하는 메서드
# @classmethod
# def print_school(cls) : #클래스 메서드
#     print("학생들은", cls.school_name, "에 다닌다!") # 클래스 변수 사용
#
# # 등교하기 위한 교통수단을 출력하는 메서드(정적 메서드)
# @staticmethod
# def print_trans() : # 정적 메서드
#     print("학생들은 버스를 타고 등교한다!")
# # 정적 메서드 호출 : 객체와 클래스를 통해 호출 가능
# st1.print_trans()
# Student.print_trans()
# # 부모클래스
# class Person :
#     # 부모 클래스의 생성자
#     def __init__(self, name) :
#         self.name = name # 데이터 속성
#         #메서드
#     def eat(self, food) :
#         print(self.name, "이/가", food,"를 먹습니다.")
#
# #Person 클래스를 상속받는 자식 클래스 생성
# class Student(Person) :
#     # 자식 클래스의 생성자
#     def __init__(self, name, school) :
#         # 부모클래스의 생성자 호출
#         super().__init__(name) # 부모의 생성자 매개변수 name에 값을 전달
#         self.school = school # 자식 클래스에 추가된 데이터 속성
#
#     # 자식클래스에서 추가할 메서드
#     def study(self):
#         print(self.name, "은/는", self.school, "에서 공부합니다.")
#
# # 부모클래스의 객체
# pr1 = Person("홍길동")
# pr1.eat("떡볶이")
# #pr1.study() # 자식 클래스에서 새롭게 추가된 속성은 부모 클래스의 객체에서 사용 불가
#
# # 자식 클래스 객체 생성
# st1 = Student("짱구", "python학교")
# st1.study()
# st1.eat("감자") # 자식 클래스의 객체로 부모클래스에서 상속받은 메서드 호출

# num1 = int(input("첫 번재 정수 입력: "))
# num2 = int(input("두 번째 정수 입력: "))
#
# print(num1 / num2)
# print("출력끝!")

# try - except 구조
try:
    # 예외가 발생될 것으로 예상되는 문장
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    print(num1 / num2)

except ZeroDivisionError:
    # try 블록에서 ZeroDivisionError가 발생했을 때 실행할 문장
    print("0으로 나눌 수 없습니다.")

except ValueError :
    # try 블록에서 ValueError가 발생했을 떄 실행할 문장
    print("정수를 입력해주세요")

except Exception : # Exception은 모든 예외 클래스의 부모 클래스
    print("알 수 없는 예외가 발생했습니다.")

# try - except - else - finally 구조
try:
    li = ["a","b","c","d","e"]
    print(li[0])
    print(li[10]) # indexError 발생
    print("try영역 전체 실행 완료!")
except:
    #try영역에서 예외가 발생했을 때 실행할 문장
    print("except문 실행")

else :
    # try영역에서 예외가 발생하지 않았을 때 실행할 문장
    print("else문 실행")

finally :
    # try 영역에서 예외 발생 유무에 상관없이 실행
    print("finally문 실행")


