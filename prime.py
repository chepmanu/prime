def is_prime(n):
    numbers = []
    int(n)
    if not str(n).isdigit:
        raise ValueError("Input should be a number")
    if n < 2:
        raise ValueError("There is no prime number less that 2")

    def check_prime(number):
        for i in range(2, number):
            if not number%i:
                return
        numbers.append(number)
    for x in range (2, n + 1):
        check_prime(x)

    return numbers
print is_prime(2)