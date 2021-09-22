n = int(input())


def squares(number):
    i = 1
    while i <= number:
        yield i ** 2
        i += 1


# Don't forget to print out the first n numbers one by one here
for square in squares(n):
    print(square)
