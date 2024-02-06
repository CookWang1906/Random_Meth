#completed
n = int(input('Please input your numnber here: '))
while n < n*n:
    if n % 2==0:
        n = n/2
        print('Divi', n)
    else:
        n = n*3 + 1
        print('Muti', n)
    if n == 1:
        break