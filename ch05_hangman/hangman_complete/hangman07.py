import random

from ch05_hangman.hangman04 import end_of_game
from hangman_arts import * # hangman_arts 파일의 전체 데이터를 가지고 온다는 의미
from hangman_word_list import word_list
# hangman_word_list 파일에서 word_list 변수만 가지고 오겠다는 의미

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append('_')

end_of_game = False
while not end_of_game:
    printk(stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()