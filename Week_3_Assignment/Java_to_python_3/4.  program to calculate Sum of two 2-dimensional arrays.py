def sum_2d_arrays(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

# User input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter first 2D array:")
arr1 = [list(map(int, input().split())) for _ in range(rows)]

print("Enter second 2D array:")
arr2 = [list(map(int, input().split())) for _ in range(rows)]

result = sum_2d_arrays(arr1, arr2)
print("Sum of the two 2D arrays:")
for row in result:
    print(row)
