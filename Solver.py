

from collections import OrderedDict
# trying to set the pivot values equal to 1 and all other indices to 0.
def make_pivot(i,n,matrix,rank,inverse_matrix):
    r = rank
# Since we use doubles, using "=" might be a problem while conducting row operations.
    if matrix[i][i] <= 0.000000000001 and matrix[i][i] >= -0.000000000001:
        matrix[i][i] == 0
        #finding the pivot row
        if not change_rows(i, n, matrix,inverse_matrix,r):
            r -= 1
        else:
            make_pivot(i,n,matrix,r,inverse_matrix)
    # We should make the pivot value 1.
    elif matrix[i][i] != 1:
        divisor = matrix[i][i]
        matrix[i][n] /= divisor
        for j in range(n):
            matrix[i][j] /= divisor
            if r == n:
                inverse_matrix[i][j] /= divisor
        matrix = eliminate(i, n, matrix,inverse_matrix,r)
    else:
        matrix = eliminate(i, n, matrix,inverse_matrix,r)
    return r
# Finds the pivot row.(If it is possible)
def change_rows(i,n,matrix,inverse_matrix,rank_A):
    for j in range (i+1,n):
        if matrix[j][j] != 0:
            if  rank_A<n:
                temp1 = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = temp1
            else:
                temp1 = matrix[i]
                temp2 = inverse_matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = temp1
                inverse_matrix[i] = inverse_matrix[j]
                inverse_matrix[j] = temp2
            return True
    return False
# Does row operations in order to make all the values of the related column of the pivot 0.
def eliminate(i,n,matrix,inverse_matrix,rank):
    for j in range(n):
        rate = matrix[j][i]/matrix[i][i]
        if rank == n:
            if j != i:
                for k in range(n):
                    matrix[j][k] -= (matrix[i][k]*rate)
                    inverse_matrix[j][k] -= (inverse_matrix[i][k]*rate)
                matrix[j][n] -= (matrix[i][n]*rate)
        else:
            if j != i:
                for k in range(i, n+1):
                    matrix[j][k] -= (matrix[i][k]*rate)
    return matrix

def solve(file):
    case = 0
    matrix = []
    inverse_matrix = []
    for line in file:
        matrix.append([float(n) for n in line.strip().split(" ")])
    n = int(matrix.pop(0)[0])
    rank_A = n
    for i in range (n):
        inverse_matrix.append([0.0]*n)
        inverse_matrix[i][i] = 1.0

    for i in range(n):
        rank = make_pivot(i,n,matrix,rank_A,inverse_matrix)

    solution = OrderedDict()
    arbitrary_var = OrderedDict()
    for i in range(n):
        solution["x"+str(i+1)] = "0"

    for i in range(n-1,-1,-1):
        if matrix[i][i] == 1:
            solution["x"+str(i+1)] = str(matrix[i][n])
        else:
            if matrix[i][n] != 0:
                print("Inconsistent problem")
                print()
                case = 2
                break
            else:
                solution["x" + str(i+1)] = "0"
                arbitrary_var["x" + str(i+1)] = "0"
                case = 1
    #Unique solution
    if case == 0:
        print("Unique solution:",end = " ")
        for key in solution:
            print(key+" = " + solution[key],end=" ")
        print()
        print("Inverted A: ",end = "")
        for row in inverse_matrix:
            print(*row)
        print()
    #Arbitrary Solution
    elif case == 1:
        print("Arbitrary variables:",end = " ")
        for key in arbitrary_var:
            print(key+" = " + arbitrary_var[key],end = " ")
        print()
        print("Arbitrary solution:",end = " ")
        for key in solution:
            print(key + " = " + solution[key], end=" ")
        print()
        print()


if __name__ == '__main__':
    file_1 = open('Data1.txt', 'r')
    file_2 = open('Data2.txt', 'r')
    file_3 = open('Data3.txt', 'r')
    file_4 = open('Data4.txt', 'r')
    solve(file_1)
    solve(file_2)
    solve(file_3)
    solve(file_4)
    file_1.close()
    file_2.close()
    file_3.close()



