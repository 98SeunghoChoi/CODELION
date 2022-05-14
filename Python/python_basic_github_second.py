# 2강
    # python 함수 작성하는 법
    # def ------- ():
    #     print(1. ----)
    #     print(2. ----)
    #     print(3. ----)
    #         이런 형식으로 만들어주면 됨.
    # 그리고 불러올 때는 
    # ---------() 작성한 후 -> terminal 에서 python lecture.py 이런 식으로 작성하게 되면 def에서 나오는 것처럼 결과값이 도출되게 됨

#3강
    # dictionary = {"key" : "value"} 라고 부름
    #               질문  /  대답
    #               취미  / 영화보기
    #               특기  / 배드민턴
    # 두 가지 형태로 dictionary를 만들 수 있음
    # 1번째 형태
    # [
    #   {"질문":"취미", "대답":"영화보기"}
    #   {"질문":"특기", "대답":"배드민턴"}
    # ]
    # 2번째 형태
    # 
    # {"취미":"영화보기"}
    # {"특기":"배드민턴"}

# 4강
#     total_dictionary = {}

#     while True:
#         question=input("질문을 입력해주세요 : ")
#         if (question == "q"):
#             break
#         else: 
# #             total_dictionary[question] = "" /total_dictionary[question] = "" -> 좌변 [] 안에는 key / = 우변 "" 안에는 value

# 5강
    # total_dictionary = {} / dictionary 형태는 {}

    # while True:
    #     key = input("질문을 입력해주세요 : ") 
    #     if key == "q":
    #         break
    #     else: 
    #         total_dictionary[key] = "" / dictionary 형태의 .append -> [key] = "value"가 들어감

    # for i in total_dictionary: / 위에 있는 것을 한 번 반복한 것
    #     value = input("답변을 입력해주세요 : ")
    #     total_dictionary[i] = value
    # print(total_dictionary)

# 6강
    # <질문 부분>
    # total_list = []

    # while True: 
    #     question = input("질문을 입력해주세요 : ")
    #     if question == "q":
    #         break
    #     else: 
    #         total_list.append({"질문" : question, "답변" : ""})
    # 질문 적은 것만 불러오고 싶을 때 print(i["질문"])
# 7강 

# total_list = []

# while True:
#     question = input("질문을 입력해주세요 : ")
#     if question == "q":
#         break
#     else: 
#         total_list.append({"질문" : question, "답변" : ""})
# for i in total_list:
#     print(i["질문"])
#     answer = input("답변을 입력해주세요 : ")
#     i["답변"] = answer
# print(total_list) -> 근데 뭔가 굉장히 비효율적인 방법이라고 생각했음.

# 8강

# #total_list = []

# while True:
#     question = input("질문을 입력해주세요 : ")
#     if question == "q":
#         break
#     else: 
#         total_list.append({"질문" : question, "답변" : ""})
# for i in total_list:
#     print(i["질문"])
#     answer = input("답변을 입력해주세요 : ")
#     i["답변"] = answer
# print(total_list)