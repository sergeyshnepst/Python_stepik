n = int(input())
matrix = []
flag = "YES"
def magic_square(n):
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    exp_num = int(n * (n * n + 1) / 2)

    all_numbers = set(range(1, n * n + 1))
    matrix_numbers = set()
    for row in matrix:
        matrix_numbers.update(row)
    if matrix_numbers != all_numbers:
        return "NO"       

    for i in range(n):
        row = []
        for j in range(n):
            row.append(matrix[i][j])
        if sum(row) != exp_num:
            return "NO"

    for i in range(n):
        col = []
        for j in range(n):
            col.append(matrix[j][i])
        if sum(col) != exp_num:
            return "NO"
        
    main = []
    for i in range(n): 
        for j in range(n):
            if i == j:
                main.append(matrix[i][i])
    if sum(main) != exp_num:
        return "NO"

    slv = []
    for i in range(n):
        for j in range(n):
            if i + j + 1 == n:
                slv.append(matrix[i][n-i-1])
    if sum(slv) != exp_num:
        return "NO"

    return "YES"

print(magic_square(n))
