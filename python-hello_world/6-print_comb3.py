#prints all possible different combinations of two digits.
# The two digits must be different - 01 and 10 are considered identical.

for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            print("{:d}{:d}".format(i, j), end="")
            if i < 8:
                print(", ", end="")