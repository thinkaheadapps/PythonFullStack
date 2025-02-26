# initialize
i = 0
sum = 0

while i <= 10:
    print(i, end=" ")
    sum += i
    i += 1
print(sum)

#print even number sum
j = 0
add = 0
while j <= 10:
    if j % 2 == 0:
        add += j
    j += 1
print(add)
