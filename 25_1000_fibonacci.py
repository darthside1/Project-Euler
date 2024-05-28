def first_fibonacci_with(digit_amount):
    f1 = 1
    f2 = 1
    i = 2

    while len(str(f2)) < digit_amount:
        f1, f2 = f2, f1 + f2
        i += 1

    return i


if __name__ == '__main__':

    solution = first_fibonacci_with(1000)
    print(f'Index of the first fibonacci number with 1000 digits: {solution}')

# Correct solution: 4782
    