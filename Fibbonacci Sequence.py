def fibonacci_sequence(n):
    # defines precursor conditions
    n1 = 0
    n2 = 1
    n3 = n2 + n1
    count = 1
    # this finds the n3 value for values other than n == 1 and n == 2
    while count < n-1:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1
    # edgecases
    if n == 1:
        print(n1)
    elif n == 2:
        print(n2)
    else:
        print(n3)


fibonacci_sequence(101)
