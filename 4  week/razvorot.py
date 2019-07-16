def razvorot():
    n = int(input())
    if n != 0:
        razvorot()
        print(n)
    else:
        print(n)


razvorot()
