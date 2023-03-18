import numpy as np

matrix=np.random.randint(1,10,size=(9,9))
print(matrix)

# print(matrix[2][3])
matrix_sub=(matrix[3:6,2:7]).copy()
print(matrix_sub)

matrix_sub[0,0]=27
print(matrix_sub)
# print(matrix)

matrix_reshape=matrix_sub.T
print(matrix_reshape)
print(np.concatenate([matrix_sub,matrix_sub]))
print(np.flip(matrix_reshape))

# print(matrix[::-1,::])
# print(matrix[4])