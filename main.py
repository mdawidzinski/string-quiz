import random
import sys
from Questions import Quiz

# TODO result comparison - result would be saved after game in xlx file, but i dont know what to compare,
#  correct answer or ratio.
print('Welcome to quiz. There are a total of 15 questions. You can always end quiz by typing: quit. GL HF')
print('How many question you would like to answer?')
a = len(Quiz)
q_num = int(input('You can chose up %s questions:' % a).strip())  # create exception ?

q = random.sample(list(Quiz.items()), k=q_num)
player_correct_ans = 0

for num, (question, options) in enumerate(q, start=1):
    print('\nQuestion %s:' % num)  # is there possibility to make some delay between questions?
    print(question)
    correct_ans = options[0]
    sorted_options = random.sample(options, k=len(options))
    for label, option in enumerate(sorted_options, start=1):
        print('%s %s' % (label, option))
    player_answer = input('Your answer:').strip()
    if player_answer == "quit":
        print('Correct answers: %s, out of %s question' % (player_correct_ans, num - 1))
        sys.exit()
    while not player_answer.isdigit():  # temp exception handling, improved version in test.py waiting for improve
        print('That\'s not valid answer. Input number from 1 to 4.')
        player_answer = input('Your answer:').strip()
    player_answer = int(player_answer) - 1
    while player_answer not in range(4):
        print('That\'s not valid answer. Input number from 1 to 4.')
        player_answer = input('Your answer:').strip()
        player_answer = int(player_answer) - 1
    answer = sorted_options[player_answer]
    if answer == correct_ans:
        player_correct_ans += 1
        print('That\'s correct!')
    else:
        print('That\'s not right')
print('Correct answers: %s, out of %s question' % (player_correct_ans, num))
if player_correct_ans >= int(num * 0.8):
    print('That\'s great result')
