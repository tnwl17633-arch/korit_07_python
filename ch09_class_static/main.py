'''
1. 클래스 변수 vs 인스턴스 변수
    인스턴스 변수 : 인스턴스 마다 서로 다른 값을 가지는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수(Java에서는 정적 변수)

    인스턴스 변수
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(x)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(o)
'''
# from ch07_classes.main import person01

# 클래스 변수 예시
# class Korean:
#     country = '한국'
#     # 인스턴스 변수의 경우는 생성자 내부에 있었습니다.(__init__ 내부).
#     # 클래스 변수는 이상처럼 클래스 내부에 선언하고 초기화하면 됩니다.
#
#     def __init__(self, name, age, address):
#         self.name = name            # 인스턴스 변수 # 1
#         self.age = age              # 인스턴스 변수 # 2
#         self.address = address      # 인스턴스 변수 # 3
#
# # 객체 생성
# man1 = Korean('김일', 21, '서울특별시 종로구')
# print(man1.name)
# print(man1.age)
# print(man1.address)
#
# print(man1.country)     # 결과값 : 한국
# print(Korean.country)   # 결과값 : 한국

'''
객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 하지만, 클래스 내부의 코드를 들여다보기 전까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없다는 문제가 있습니다.

이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는 클래스명.클래스변수명을 통해서 참조하는 것이 권장됨.

2. 클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
# class Korean2:
#     country = '대한민국'   # 클래스 변수의 선언 및 초기화
#
#     # 클래스 메서드 정의 방법
#     @classmethod                # @classmethod 데코레이터를 달면 클래스 메서드로 인지함.
#     def trip(cls, travelling_site):     # 그 결과 첫 번째 매개변수가 self가 아니라 cls
#         if cls.country == travelling_site:
#             print('국내 여행 입니다.')
#         else:
#             print('해외 여행 입니다.')

# Korean2.trip('대한민국')
# Korean2.trip('미국')
# man2 = Korean2()
# man2.trip('일본')
# 클래스 변수와 마찬가지로 객체명.클래스메서드명()으로 호출이 가능하기는 하지만 마찬가지로 이게 인스턴스 메서드인지 알 바가 아니기 때문에 클래스메서드를 호출할 때는 # 클래스명.클래스메서드명()으로 하는 것이 권장됩니다.

'''
특징 : 
    1) 인스턴스 / 클래스로 호출 가능 -> 하지만 클래스로 호출하도록 권장
    2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출하면 되니까)
    3) @classmethod 데코레이터(decorator)를 표시하고 작성
    4) 매개변수 cls를 사용 -> self는 객체를 의미하고 / cls는 클래스를 의미
    
    
3. 정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 -> 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미.  self.속성명을 사용하여 인스턴스 변수의 값을 참조하는데 정적 메서드는 아예 첫 번째 매개변수가 고정이 아닙니다 - 클래스 메서드와의 공통점 # 1
    
    인스턴스를 생성하지 않아도 사용할 수 있음 - 클래스 메서드와의 공통점 # 2
    
    특징 : 
        1) 인스턴스 / 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 # 1
        4) 반드시 작성해야 할 매개변수(self / cls)가 없음 -> 클래스 메서드와의 차이점 # 2
        
이상을 토대로, 정적 메서드는 self / cls를 둘 다 사용하지 않기 때문에 인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적합.
정적 메서드 자체는 클래스에 소속돼있지만 인스턴스에는 영향을 주지도 않고 받지도 않음.

즉 Java에서의 정적 메서드 = 파이썬의 클래스 메서드 + 정적 메서드
'''
# class Korean3:
#     country = '한국'      # 클래스 변수
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea! ')
#
#     @staticmethod
#     def slogan2(str_example):
#         """얘는 그냥 매개변수가 있는 애입니다."""
#         print('Imagine Your Korea!' + str_example)
#
#
# Korean3.slogan()
# korean3.slogan2('근데 너무 덥다')
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의할겁니다.
'''
# 클래스 정의
# class Bag:
#     # 클래스 변수의 선언 및 초기화
#     count = 0
#
#     def __init__(self): # 생성자 호출 및 인스턴스 변수들 정의할 용도. 그럼 생성자도 인스턴스 변수라고 할 수 있겠네요(self가 있으니까)
#         Bag.count += 1          # 생성자가 호출될 때마다(=객체가 생성될 때마다) 클래스 변수인 count가 1씩 증가함. cls.count가 아니라 클래스명.count라는 것에 주목해야 합니다.
#         print('가방 객체가 생성되었습니다.')
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#         # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기 때문에 Bag.count가 아니라 cls.count로 작성되었습니다.
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print(f'현재 가방 재고 : {Bag.count}')
# print(f'현재 가방 재고 : {Bag.remain_bag()}')


# 객체 생성
# bag1 = Bag()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# bag1.sell()     # 실제로 bag1객체가 사라진 건 아닌거 아시죠?
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# Bag.sell()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')

''' 
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오.

지시사항
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''
# class Person:
#     # 클래스 변수의 선언 및 초기화
#     population = 0
#
#     @classmethod
#     def get_population(cls):
#         return cls.population       # 클래스 변수를 사용한 지점
#
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1#  인스턴스 메서드를 통해서 클래스 변수를 변화 시킨 거니까 클래스명.클래스변수명
#         print(f'{self.name}이(가) 태어났습니다.')
#
#     def __del__(self):
#         Person.population -= 1
#         print(f'RIP {self.name}')
#
# print(Person.get_population())
# man = Person('김일')
# woman = Person('김이')
# print(Person.get_population())
# del man
# print(Person.get_population())
# print('프로그램 종료')
'''
다음 지시 사항을 읽고 가게의 매출을 구할수 있는 Shop 클래스를 작성하시오.
지시사항 
1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 dictionary 요소를 가진 list
    
    menu_list = [{ '떡볶이' : 3000 } , { '순대': 4000}, { '튀김': 500}, {'김밥' : 2000 }]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales('떡볶이', 1)    # 떡볶이을(를) 1개 판매
Shop.sales('김밥', 2)    # 김밥을(를) 2개 판매
Shop.sales('튀김', 5)    # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f'매출 : {Shop.get_total()}원')
'''
class Shop:
    total = 0
        menu_list = [{ '떡볶이' : 3000 } , { '순대': 4000}, { '튀김': 500}, {'김밥' : 2000 }
        menu_dict = {           # 딕셔너리 내에 pair 하나밖에 없는 상태인데, 있으면 이하의 코드라인이 실행되고 아니면 넘어갈겁니다. 그러면 다음
                                # 반복으로 가겠네요.
            # in -> element를 기준으로 해야 하기 때문에 dictionary의 element 중 'key'를 기준
            # 애초에 key 없으면 value를 조회 못하는게 dictionary의 특징 중 하나
            cls.total += menu_dict[menu_name] * quantity
            print(f'{menu_name}을(를) {quantity}개 판매')
    @classmethod
    def sales2(cls, menu_name, quantity):
        if menu_name in cls.menu_dict: # 그러면 굳이 반복문 다 돌려서 일치하는 key가 있는지 확인할 필요가 없습니다.
            cls.total += cls.menu.dict[menu_name] * quantity


        '떡볶이' : 3000,
        '순대' : 4000,
        '튀김' : 500,
        '김밥' : 2000,

    }
                                }

    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def sales(cls, para1, para2):
        pass

        for food in cls.menu_list:


print(f'매출 : {Shop.get_total()원}')

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)
print(f'매출 : {Shop.get_total()}원')






