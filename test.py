# there is some issue when input is a letter

def valid_answer(player_answer):
    print(not player_answer.isdigit())  # test purpose

    if not player_answer.isdigit:  # why this doesn't work?
        print('That\'s not valid answer. Input number from 1 to 4.')
        new_answer = input('Your answer:').strip()
        return valid_answer(new_answer)
    if int(player_answer) not in range(1, 5):  # but this dose
        print('That\'s not valid answer. Input number from 1 to 4.')
        new_answer = input('Your answer:').strip()
        return valid_answer(new_answer)
    player_answer = int(player_answer) - 1
    return player_answer


while True:
    player_answer = input('dig:')
    print(valid_answer(player_answer))