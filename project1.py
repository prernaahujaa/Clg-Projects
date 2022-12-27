import random
imagine_num, guess_num = random.randint(1, 10),0
while imagine_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
