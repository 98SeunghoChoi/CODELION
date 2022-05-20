from googletrans import Translator                  

translator = Translator()                           

sentence = input("문장을 입력해주세요 : ")               
dest= input("원하는 언어를 입력하세요 : ")                

result = (translator.translate(sentence, dest))     
detected = translator.detect(sentence)              

print("============= 출력 결과 =============")
print(detected.lang, ": ", sentence)               
print(result.dest, " : ", result.text)              
print("============= 출력 결과 =============")
