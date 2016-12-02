'''
MATRIX_ADDITION(matrixB,matrixC,cols_rows)
    for i<-0 to cols_rows.size()
        for j<-0 to cols_rows.size()
            added_matrix[i][j] <- matrixB[i][j] + matrixC[i][j]
    RETURN added_matrix
    
Big O notation: О(n*n)
'''
'''
MATRIX_SUBTRACTION(matrixB,matrixC,cols_rows)
    for i<-0 to cols_rows.size()
        for j<-0 to cols_rows.size()
            subtracted_matrix[i][j] <- matrixB[i][j] - matrixC[i][j]
    RETURN subtracted_matrix

Big O notation: О(n*n)
'''
'''
MATRIX_MULTIPLICATION(matrixB,matrixC,cols_rows)
    for i<-0 to cols_rows.size()
        for j<-0 to cols_rows.size()
            for p<-0 to cols_rows.size()
                multiplied_matrix[i][j] = multiplied_matrix[i][j]+(matrixB[i][p] * matrixC[p][j])
    return multiplied_matrix

Big O notation: О(n*n*n)
'''
'''
A <- MATRIX_SUBTRACTION(MATRIX_MULTIPLICATION(matrixB,matrixC,cols_rows),2*MATRIX_ADDITION(matrixB,matrixC,cols_rows),cols_rows)
'''
