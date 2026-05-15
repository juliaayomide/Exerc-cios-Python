print('Esse programa lê um número e informa a tabuada desse número')
num1 = int(input('digite o número: '))

for n in range(1,11):
    print(f'{num1} x {n} = {num1*n}')
