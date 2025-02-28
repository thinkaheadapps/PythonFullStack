def star_pattern(n):
    for i in range(n):
        # Print spaces - n-i-1 spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars - (2 * i + 1) stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

# Getting input from the user
n = int(input())
star_pattern(n)
