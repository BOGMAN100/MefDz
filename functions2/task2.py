def make_matrix(size, value=0):
    
    if isinstance(size, tuple):
        width, height = size
    else:
        width = height = size

    return [[value] * width for i in range(height)]


result1 = make_matrix(3)
print(result1)

result2 = make_matrix((4, 2), 1)
print(result2)

# если глаза болят, то
def print_matrix(matrix):
    for row in matrix:
        print(row)
    
result1 = make_matrix(3)
print_matrix(result1)

result2 = make_matrix((4, 2), 1)
print_matrix(result2)