def fibonacci(n):
    i = 1
    first_value = 0
    second_value = 1
    while i <= n:
        if i == 1:
            yield 0
        elif i == 2:
            yield 1
        else:
            new_value = first_value + second_value
            first_value = second_value
            second_value = new_value
            yield new_value
        i += 1
