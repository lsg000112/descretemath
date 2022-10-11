cnt = 0

def queen(row, col):
    global cnt
    n = len(col)
    if(isValid(row, col)):
        if(n-1 == row):
            if cnt < 10:
                for i in range(n):
                    a = ''
                    for j in range(n):
                        if col[i] == j:
                            a += '1 '
                        else:
                            a += '0 '
                    print(a)
                print()
            cnt += 1
        else:
            for i in range(0, n):
                col[row+1] = i
                queen(row+1, col)

def isValid(row, col):
    for i in range(0, row):
        if col[i] == col[row]:
            return False
        if abs(col[i]-col[row]) == abs(i-row):
            return False
    return True

n = int(input('n = '))
queen(-1,[0] * n)
print('total possible arrangements: ' + str(cnt))