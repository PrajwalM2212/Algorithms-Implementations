def nqueen(n, a, col):
    for row in range(n):
        if check(col, row, n, a):
            a[row][col] = 1
            if col == n - 1:
                return True
            if nqueen(n, a, col + 1):
                return True
            else:
                a[row][col] = 0
    return False


def check(col, row, n, a):
    print(row, col)
    for i in range(n):
        print(a[i], '\n')
    count = col
    for j in range(col):
        for i in range(n):
            if a[i][j] == 1:
                if i == row:
                    return False
                if j + count == col and i + count == row:
                    return False
                if j + count == col and i - count == row:
                    return False
        count -= 1
    return True


if __name__ == '__main__':
    n = int(input('Enter the size of board '))
    a = {}
    for i in range(n):
        a[i] = [0 for j in range(n)]
    print(nqueen(n, a, 0))
    # tracer = trace.Trace(count=False, trace=True)
    # tracer.run('nqueen(n, a, 0)')
    for i in range(n):
        print(a[i], '\n')
