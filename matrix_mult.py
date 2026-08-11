def dot_prod(vector_a, vector_b):
    """
    Calculates the dot product of two vectors given as list arguments.
            
    Arguments: 
        vector_a (list of floats): The first vector that will be used to calculate the dot product.
        vector_b (list of floats): The second vector that will be used to calculate the dot product.
            
    Returns:
        dot_product (float): The dot product of the two list arguments.
    """
    dot_product = 0
    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
    return dot_product


def matrix_mult(matrix_a, matrix_b):
    """
    Calculates the matrix product of two matrices given as list arguments.
            
    Arguments: 
        matrix_a (list of lists of floats): The first matrix that will be used to calculate the matrix product.
        matrix_b (list of lists of floats): The second matrix that will be used to calculate the matrix product.
            
    Returns:
        matrix_product (list of lists of floats): The resulting matrix product.
    """
    matrix_product = []

    if len(matrix_a[1]) != len(matrix_b):
        return None
    else:
        for row in range(len(matrix_a)):
            current_row = []
            for column in range(len(matrix_b[0])):
                current_row.append(None)
                a = matrix_a[row]
                b = []
                for i in range(len(matrix_b)):
                    b.append(matrix_b[i][column])
                current_row[column] = dot_prod(a, b)
                print(a, b)
            matrix_product.append(current_row)

        return matrix_product




#print(dot_prod([1, 4, 0.3, 10.23, 5], [-4, 1.6, 2, 2.2, 0]))

# Notes to self:
# The number of lists in each matrix represents the rows, and the 
# numbers they contain are the numbers in the corresponding rows.
# Additionally, the amount of numbers in each row is equal to the
# number of columns in the matrix.

#list1 = [[3,1], [-8,5], [1,4]]
#list2 = [[1,4,7,1], [-5,-8,4,3]]
#matrix_product = matrix_mult(list1, list2)
#print(matrix_product)