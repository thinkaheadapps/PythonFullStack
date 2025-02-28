# n = 4
#
# #
# # #
# # # #
rows = int(input())
for i in range(rows):
    for j in range(i):
        print("#", end=" ")
    print()


# n = 3
#
# #
# # #
for k in range(1, rows+1):
    for m in range(k):
        print("#", end=" ")
    print()
