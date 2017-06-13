def is_prime(n):
    numbers = []
    if not str(n).isdigit():
        #To check if n is an interger and if not to raise ValueError.
        raise ValueError("Input should be a number")
        
    if n < 2:
        raise ValueError("There is no prime number less that 2")

    def check_prime(number):
        #To check if the number in range is prime and add it to a list if it is.
        for i in range(2, number):
            if not number%i:
                return
        numbers.append(number)
    for x in range (2, n + 1):
        check_prime(x)

    return numbers
