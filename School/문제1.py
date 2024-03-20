sentence = input("문장을 입력하세요. : ")
user_input = input("특수문자를 입력하세요. : ")
sen_idx = len(sentence) // 2

new_sentence = sentence[:sen_idx] + user_input + sentence[sen_idx:]
print(new_sentence)
