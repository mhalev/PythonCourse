import sys

if not sys.argv[1].isdigit():
    print('Введите число.')
else:
    num_steps = int(sys.argv[1])
    for i in range(num_steps,0,-1):
        print(' '*(i-1)+'#'*(num_steps+1-i))
