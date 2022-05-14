
# 1강 #
# import random   # import를 통해 random 명령어가 실행될 수 있게 환경 조성하는 역할
# print(random.choice(["김치찌개","된장찌개","삼겹살","곱창","과자"])) #5가지 음식에 대하여 random으로 골라달라를 뜻함
# ----------------------------------------------- # # ----------------------------------------------- # 
# 2강  <for을 통해 30번 반복 / while 무한루프 + while 멈추는 2가지 방법 

# import random
# for x in range(30):
#     print(random.choice(["김치찌개","된장찌개","삼겹살","곱창","과자"]))
# ----> 두 번째 문장 들여쓰기 ****** 중요 
# import random

# while True:
#     print(random.choice(["김치찌개, 된장찌개", "삼겹살", "곱창", "과자"]))
#     print("이 문장까지 반복이 될까")

# break 명령어를 써주면 실행되던 게 멈춤
# time.sleep(1) -> 반복문이 한 번 실행된 후 (1)초 동안 기다렸다가 다음 반복이 진행되는 명령 
# ---------------------------------------------------------------
# 5강 점심 저녁 
# import random
# lunch = print(random.choice(["된장찌개", "피자", "제육볶음"]))
# dinner = print(random.choice(["된장찌개", "피자", "제육볶음"]))
# print(lunch) -> #(lunch = 변수)에 속해있는 내용물이 나오는 것.
# 대신 lunch = "냉장고"를 이후에 적게 되면 lunch 안에 있던 print는 사라지고 냉장고만 남게 됨
#  -------------------------------------------------------------------

# 6강 dictionary 
# information = {"고향":"수원", "취미":'영화보기',"좋아하는 음식":"국수"}
# print(information)
# 결과값 그대로 출력됨 하지만 중요한 건 이게 아님
# print(information.get("") 이런식의 형태로 변수 안에 저장된 dictionary에 대한 값 출력 가능!
# ----------------------------------------------------------------------------
# 7강 심화
# <dictionary 심화> 
# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# print(information.get("취미"))
# information["특기"] = "피아노" / dictionary에 해당 값 추가
# information["사는곳"] = "서울" / dictionary에 해당 값 추가
# del information["좋아하는 음식"]
# print(len(information))
# information.clear() / 전체 삭제
# print(foods[0])


# <List 심화>
# foods = ["된장찌개", "피자", "제육볶음"]
# print(list[0]) -> 된장찌개
# print(list[-1]) -> 제육볶음
# foods.append("김밥") = list에 항목 추가
# del foods[0] -> 이런 식으로 적혀있는데 del을 쓸 때는 [] 안에 숫자가 적혀야만 함
# -----------
# <8강 >

# food = ["된장찌개", "피자", "제육볶음"]
# 전수업에서 배운 내용은 for x in range(3):
#                         print(X)
#                         만약 dictionary와 list에서 수정할 것들이 생길 경우 이러한 수식을 사용했다면 수정하기 전 결과값이 출력됨
# for x in food:
#     print(x) 이렇게 해주면 수정된 부분들까지 추가되어 전부 출력가능
# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# for x, y in information.items(): / dictionary에는 이런 식으로 마지막에 마무리 지어줘야 가능
#     print(x)
#     print(y)

# ----------------------
# <9강 집합>
# foods = ["된장찌개", "피자", "제육볶음"]
# foods_set1 = set(foods)
# foods_set2 = set(["된장찌개", "피자", "제육볶음"])
# print(foods_set1)
# print(foods_set2)
# /// list 와의 차이점 : list는 안에 들어가있는 각각의 순서가 존재하지만 집합에는 존재하지 않음
# /// 그래서 결과값이 리스트와 차이점이 생기는데 고정값인 리스트와 다르게 set(집합)은 랜덤으로 순서가 결정됨

# --------------
# <10강 집합 확장>

# foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
# foods_set = set(foods)
# print(foods)
# print(foods_set)

# # 결과값이 다르게 나옴 집합은 교집합이 생길경우 알아서 한개로 줄여줌
# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 | menu2 -> 합집합
# menu4 = menu1 & menu2 => 교집합
# menu5 = menu1 - menu2 => 차집합
# print(menu3)

# ----------------
# < 11강 만약에> 
# import random
# print(food)
# food = random.choice(["된장찌개", "피자", "제육볶음"])
# if(food == "제육볶음"):
#     print("곱배기 주세요")
# else:    
#     print("그냥 주세요")
# print("종료") -> 이런식으로 조건문을 만들어줄 수가 있음.

# ----------------
# <12강 + 13강 프로덕트> 

# lunch = ["라면", "된장찌개", "피자", "치킨"]

# while True: 
#     print(lunch) -> 어떤 메뉴가 있는지 알아보고 쉽게
#     item = input("메뉴를 입력해주세요 : ") -> item이라는 변수에 input을 대입
#     if (item == "q"): item 값에 q를 입력하면 break
#         break
#     else:
#         lunch.append(item) -> 아닐 경우에는 메뉴를 추가할 수 있게끔 만들어줌
# print(lunch)

# set_lucnh = set(lunch) -> lunch를 집합화시키는 것

# < 14강>
# 차집합, 교집합, 합집합은 모두 집합인 변수끼리간 연산이 가능(그래서 list -> set) 이런 식으로 연산해야함


# lunch = ["라면", "된장찌개", "피자", "치킨"]

# while True: 
#     print(lunch)
#     item = input("메뉴를 입력해주세요 : ")
#     if (item == "q"):
#         break
#     else:
#         lunch.append(item)
# print(lunch)

# set_lucnh = set(lunch)

# <15강_최종>

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
# # random.choice는 list에서만 작동 가능
# 작성하기 어려워서 코드라이언 15강 작성하기_혼자 작성 가능했음 지금은
