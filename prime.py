def is_prime(n):
    numbers = []
    if n < 2:
        return

    def check_prime(number):
        for i in range(2, number):
            if not number%i:
                return
        numbers.append(number)
    for x in range (2, n + 1):
        check_prime(x)

    return numbers
