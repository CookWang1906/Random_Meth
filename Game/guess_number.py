#status: Completed
#info: Test your luck by guessing number. Good luck!

import random
numbers = random.randint(1, 10)
n = int(input('Pick a number from 1 to 10: '))
if n == numbers:
    print('Congratulations, You won!!!')
else:
    print('Oh, Better luck next time!!')