N = int(input("enter the digit:"))

for i in range(0, N):

    if i == 0: 

        print('  '* (N-1) + '*')

    elif i == N - 1: 

        print('* ' * N)

    else:
        left_spaces = '  ' * (N -i-1)

        hollow_spaces = ('  ' * ( i - 1))