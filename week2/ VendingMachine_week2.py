# [1] 아메리카노 2500원  [2] 카페라떼 3000원 [3] 카푸치노 3700원


print ("[1] 아메리카노 2500원  [2] 카페라떼 3000원 [3] 카푸치노 3700원")
menu = int (input("주문할 메뉴를 선택하세요>> "))
cup = 0     # 메뉴의 잔 수
price = 0
money = 0

if menu < 1 or menu > 3 :
    print("없는 메뉴를 선택하여 종료합니다.")
    exit(1)
elif menu == 1:
    cup = int(input("아메리카노 몇 잔? "))
    price = cup * 2500
elif menu == 2:
    cup = int(input("카페라떼 몇 잔? "))
    price = cup * 3000
elif menu == 3:
    cup = int(input("카푸치노 몇 잔? "))
    price = cup * 3700

print("총 금액은 ", price, "원입니다.")
money = int(input("돈을 입력하세요>> "))
if price > money:
    print("돈이 부족하여 종료합니다.")
    exit(1)
else:
    changeMoney = money - price
    print("거스름돈 ", changeMoney, "원을 받으세요")
    w1000 = changeMoney // 1000
    changeMoney = changeMoney % 1000    # changeMoney = 500
    w500 = changeMoney // 500
    changeMoney = changeMoney % 500
    w100 = changeMoney // 100
    print("1000원 = %d" % w1000)
    print("500원 = ", w500)
    print(f"100원 = {w100}")
