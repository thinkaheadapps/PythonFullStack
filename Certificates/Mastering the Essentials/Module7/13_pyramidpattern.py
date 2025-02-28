rows = int(input())  # Input the number of rows

for j in range(rows):
    # Print spaces: Decrease as the row number increases
    print(" " * (rows - j - 1), end="")

    # Print stars: Increase as the row number increases
    print("*" * (2 * j + 1))
