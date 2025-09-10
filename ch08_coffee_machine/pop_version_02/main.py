from ch04_functions.main import drink_price

MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5
    },
    '라뗴': {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    }
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}


# 함수 정의 영역
def is_resources_enough(
        order_ingredient):  # 만약에 특정 함수/메서드의 결과값이 boolean이라면 대개 다음 조건문/반복문의 조건식으로 쓰이는 경우가 많습니다. 함수형 프로그래밍 개념을 떠올리시면 됩니다.
    """
    DocString : 함수 / 클래스 / 메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능.
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면 True 반환, 아니면 False 반환
    :param : order_ingredient
    :return : True / False
    """

    for item in order_ingredient:  # order_ingredient의 자료형은 무엇이고, 그 근거는?
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True


def process_coins():

    sum = 0

    # 근데 지금 함수 하나에 지역 변수가 5개나 있다는 사실을 알 수 있습니다.
    # 그리고 다수의 수강생분들이 빡세게 collections 쓰는 바람에 내부에 조건문이 있거나
    # 반복문이 있는 경우도 있습니다.
    sum += float(input('쿼터 동전을 몇 개나 넣으시겠습니까? >>> ')) * 0.25
    sum += float(input('다임 동전을 몇 개나 넣으시겠습니까? >>> ')) * 0.1
    sum += float(input('니켈 동전을 몇 개나 넣으시겠습니까? >>> ')) * 0.05
    sum += float(input('페니 동전을 몇 개나 넣으시겠습니까? >>> ')) * 0.01
    return sum


# todo - 6 : 우리가 왜 동전 처리 함수를 정의했는지 이해해야합니다. 해당 총합을 가지고, 총합이 '선택한' 음료 가격보다 높다면 다음 과정으로 넘어갈 필요가 있습니다.
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아 받은 동전의 총합이 음료 가격보다 높으면 True / 아니면 False 반환. 그리고 True인 경우에는 profit에 음료 가격만큼 추가해줘야 하고, False인 경우에는 받은 동전들을 반환해주는 안내문 출력"""
    change = money_received - drink_cost
    if change >= 0:
        # 이러면 음료 제조 과정으로 넘어가야겠네요. 그리고 profit에 추가도 해줘야 하고.
        global profit
        profit += drink_cost
        print(f'잔돈 ${change}을(를) 반환합니다.')
        return True  # 그래야 음료 제조 과정의 조건식으로 쓸 수 있으니까요
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False  # 얘는 음료 제조 과정의 조건식으로 쓰이더라도 실행이 안되겠네요.


def make_coffee(drink_name, order_ingredient):
    """

    resources에 있는 재료에서 메뉴['음료명']['재료']들을 차감함.
        -> 차감은 is_resources_enough()이 True였기 때문에 무조건 0이상이 나옵니다.
    :param drink_name: str
    :param order_ingredient: dict
    :return: none -> call2() 유형으로 작성하겠습니다.
    """
    for item in order_ingredient:  # resources가 아니라 order_ingredient를 반복문 돌리는 이유는 에스프레소 일 때 오류가 발생하기 때문입니다. 에스프레소의 재료에는 우유가 없는데 resources에는 있는 상태가 되죠. 그래서 order_ingredient['우유'] 부분에서 오류가 발생하게 됩니다.
        resources[drink_name] -= order_ingredient[item]
    print(f'{choice}이(가) 나왔습니다. 맛있게 드세요 !! ♥☕')


# 관련 변수 선언 및 초기화
is_on = True
choice = ''
while is_on:
    # 반복문 내부에서 입력 받아야 하니까 여기다가 선언 및 초기화를 하겠습니다.
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    # todo - 2 만약에 choice 변수에 들어간 데이터가 'off'라면 반복문을 종료하도록 나머지 코드를 작성하시오.
    if choice == 'off':
        is_on = False  # 이번 반복은 전부 실행되고 다음 반복에서 종료
        print('자판기가 종료되었습니다.')
        # break       # 바로 종료
    # todo - 3 : 사용자가 프롬프트에 "report"를 입력하면 현재 자원 값을 보여주는 보고서를 생성합니다.
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}ml')
        print(f'돈 : ${profit}')
    # todo - 4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나일 때 작성하는 부분
    elif choice in ['에스프레소', '라떼', '카푸치노']:
        drink = MENU[choice]            # 세 번 ㅏㄴ와서 refactoring 예시로 남겨둠
        if is_resources_enough(MENU[choice]['재료']):
            money_received = process_coins()
            # 여기의 money_received는 전역 변수입니다. 그리고 process_coins()의 결과값을 변수에 담았네요.
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                make_coffee(drink_name= choice, order_ingredient= drink['재료'])

                # resources['재료']['물'] -= MENU[choice]['재료']['물']
                # resources['우유'] -= MENU[choice]['재료']['우유']
                # resources['커피'] -= MENU[choice]['재료']['커피']
                # print(f'{choice}이(가) 나왔습니다. 맛있게 드세요 !! ♥☕')
        # if choice == '에스프레소':
        #     for key in resources:
        #         resources[key] -= MENU['에스프레소']['재료'][key]
        #         if resources[key] < 0 :
        #             print(f'{key}가 부족합니다.')

    # todo - 5 : choice가 이상의 조건을 충족하지 않을 때 ' 잘못 입력하셨습니다. 다시 입력하세요'를 출력하는 부분
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요.')
'''
현재 자판기 내에 있는 물 / 우유 / 커피 / 금액에서 라떼 한 잔을 뽑고 나서의 물 / 우유 / 커피 / 금액의 변동을 콘솔에 출력하시오.

실행 예
물 : xml
우유 : xml
커피 : xg
수익 : $x

'''

# profit += MENU['라뗴']['가격']
#     print(f'수익 : ${profit}')
#     print(f'물 : {resources}')
#     print(f'우유 : {resources}')
#     print(f'커피 : {resources}')

# resources['물'] -= MENU['라떼']['재료']['물']
# print(f'물 : {resources['물']}')

# for i in range ['라떼']['재료']['물']:

# 반복문 version
# for key in resources:   # 저는 dict 반복문 돌릴 때 안 헷갈리게 변수명을 그냥 key로 쓰는 편입니다. list/tuple일 때는 i를 쓰겠죠.
#     resources[key] -= MENU['라뗴']['재료'][key]
#     if key == '커피':
#         print(f'{key} : {resources[key]}g')
#     else:
#         print(f'[key] : {resources[key]}ml')

