matrix=[[2,0,0,0],
        [9,0,77,0],
        [0,0,5,0],
        [0,44,0,6]]
print('Input Matrix : ')
for i in matrix:
    for j in i:
        print(j, end =" ")
    print()
sparseMatrix=[]
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j]!=0:
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")            
for i in sparseMatrix:
    for j in i:
        print(j, end = " ")
    print()
