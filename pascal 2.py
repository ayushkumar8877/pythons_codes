def generate_pascal_triangle(num_rows):
    triangle = []
    for row in range(num_rows):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        triangle.append(current_row)
    return triangle
num_rows = int(input("Enter the number of rows for Pascal's triangle: "))
triangle = generate_pascal_triangle(num_rows)
for row in triangle:
    print(' '.join(str(num) for num in row))