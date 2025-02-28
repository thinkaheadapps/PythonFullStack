# these statements are used to alter the flow of program
# Break: Breaks the flow of program once this condition is hit
# Continues: It skips that particular iteration
# Pass: To avoid syntax error

for i in range(1, 10):
    if i == 5:
        break
    print(i)

for j in range(1, 10):
    if j == 6:
        continue
    print(j)

