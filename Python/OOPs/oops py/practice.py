rows=3
columns=5

# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

arr=[[0 for x in range(columns)] for row in range(rows)]


for row in range(rows):
    for col in range(columns):
        arr[row][col]=row*col

arr