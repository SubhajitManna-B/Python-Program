def sum_of_diagonals(matrix):
    primary_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    secondary_diagonal_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(len(matrix)))
    return primary_diagonal_sum + secondary_diagonal_sum

# User input
rows = int(input("Enter number of rows/columns (for a square matrix): "))
print("Enter matrix elements row by row:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

print(f"Sum of diagonal elements: {sum_of_diagonals(matrix)}")
