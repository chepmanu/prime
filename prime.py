def is_prime(n):
    t = True 
    for i in range(2, n):
       if n%i == 0:
           t = False
           break # ends the for loop
       # no else block because it does nothing ...


    if t:
        print "prime"
    else:
        print "not prime"
is_prime(63)		
