#completed
import random
numbers = random.randint(1, 10)
numb = int(input('Pick a number from 1 to 10: '))
if numb == numbers:
    print('Congratulations, You won!!!')
else:
    print('Oh, Better luck next time!!')