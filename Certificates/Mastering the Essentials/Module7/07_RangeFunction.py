# range() function allows user to generate series of numbers
# iIt is iterable as well

# range(start,end,jump), range(n) - it will give no from 0 to n-1
# in range function start is included and end is excluded

# only one parameter - Start is Zero and jump is one
# Here start is 0 and jump is 1
print(list(range(5)))

# Start and end
# By default jump here will be 1
print(list(range(1, 5)))

# Start is included and end is excluded and jump is 2
print(list(range(1, 10, 2)))

# empty list
print(list(range(10, 1, 1)))  #[]

# Negative jump
print(list(range(10, 1, -1)))  #[10, 9, 8, 7, 6, 5, 4, 3, 2]

# Negative nu,bers
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]










