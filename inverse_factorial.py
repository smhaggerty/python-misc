def inverse_factorial(n):
    #if the input number is the result of evaluating a factorial number, it will
    # return the associated factorial number. If the input number is not the
    # result of evaluating a factorial then it will return the largest factorial
    # that, when evaluated, is still smaller than the input number

    divisor = 1
    total = n
    while total > 1.0:
        total = total / divisor
        if total == 1.0:
            return divisor
        divisor += 1
        print(total, divisor)
    divisor -= 2
    return divisor
