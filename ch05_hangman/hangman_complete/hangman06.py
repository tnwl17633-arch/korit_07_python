import random
import hangman_arts                     # 이게 파일명이라는 사실에 주목
import hangman_word_list                # 해야겠네요
# 즉 logo / stages와 같은 변수는 아닙니다.


# 외부의 hangman_word_list에 있는 word_list를 참조해서 저희는 chosen_word를 만들 필요가 있습니다.
# 모듈명.변수명으로 외부 파일의 데이터를 가져올 수 있습니다.

print(hangman_arts.logo)
chosen_word = random.choice(hangman_word_list.word_list)
print(chosen_word)

lives = 6
display = []
