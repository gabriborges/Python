import numpy as np

def swap_columns(array, index1, index2):
  array[:,[index1, index2]] = array[:,[index2, index1]]


# Create a NumPy array
array = np.array([[1, 2, 3],
                 [4, 5, 6], 
                 [7, 8, 9]])

# Swap the second and third columns
swap_columns(array, 1, 2)

print(array)  # Output: [[1, 3, 2], [4, 6, 5], [7, 9, 8]]
