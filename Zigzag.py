def zigzag_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()  
rows = int(input('enter the number of rows'))
columns=int(input('enter the number of columns'))
zigzag_pattern(rows, columns)
