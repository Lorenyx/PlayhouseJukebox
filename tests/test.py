def fun():
    num = 0
    while True:
        if num > 10:
            return
        yield num
        num+=2



it = fun()

print([i for i in it])