import time
import random

lunch = ["된장찌개", "피자", "치킨"]

while True:
    print(lunch)
    item = input("메뉴를 입력해주세요 : ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if (item == "q"):
        break
    else: 
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
                    #  -> 이렇게 하면 한 줄로 나오게 됨
print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)

print(random.choice(list(set_lunch)))