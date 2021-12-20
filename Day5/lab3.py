#write a python program to guess a number
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10 until you get it right : '))
    print('well guessed!')
target_num = random.randint(1,10)
guess_num = 0