st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')
# Ask user for grid size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print(f"Enter the grid row by row (each row should be {cols} characters long):")

# Create the grid from user input
grid = []
for i in range(rows):
    while True:
        row_input = input(f"Row {i + 1}: ")
        if len(row_input) == cols:
            grid.append(list(row_input))
            break
        else:
            print(f"Please enter exactly {cols} characters.")

# Rotate and print the character picture grid
print("\nRotated Grid:")
for col in range(cols):
    for row in range(rows):
        print(grid[row][col], end='')
    print()
