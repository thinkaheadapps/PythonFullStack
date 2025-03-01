s = "Example"
print(s[2])

singleLine = "This is single line"
print(type(singleLine))
print(singleLine)

multLine = """
This
is
Multiline
String
"""
print(multLine)

s1 = s + s[0]
print(s1)

# String Immutability
temp = "String is Immutable"
s2 = "G" + temp[10]
print(s2)

#Deleting a String
del s2

# Updating a String
s = "hello Divya"
s1 = "H" + s[1:]
print(s1)

#REplace Divya with test user

#Accessing characters in Python String

print(s[6])

# Access string with Negative Indexing
# # Accesses 10th character from end:
print(s[-10])

# String Slicing
# Slicing is a way to extract portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
t3 = "GeeksforGeeks"
# Retrieves characters from index 1 to 3: 'eek'
print(t3[1:4])

# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])

# Retrieves characters from beginning to index 2: 'Gee'
print(t3[:3])

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(t3[3:])

#reverse a string
print(t3[::-1])

#To update a part of string we need to create a new string since strings are immutable.










