import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for _ in range(len(chosen_word)):
    display.append('_')

guess = input('알파벳을 입력하세요 >>> ').lower()
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        print('정답')
    else:
        print('오답')
