import array

def create_2d_array(rows, cols):
    # Initialize a 2D array with zeros
    arr = [array.array('i', [0] * cols) for _ in range(rows)]
    return arr

# Example usage
rows, cols = 5, 5
two_d_array = create_2d_array(rows, cols)
for row in two_d_array:
    print(row)
# insert 1 to 12 in the 2D array
val = 1
for i in range(rows):
    for j in range(cols):
        two_d_array[i][j] = val
        val += 1
print("After inserting values:")
for row in two_d_array:
    print(row)



# In this example, we have created a 2D array with 3 rows and 4 columns.
# We have initialized the 2D array with zeros and then inserted values
# from 1 to 12 in the 2D array. Finally, we print the 2D array to display.
