def QuantifiersExample_3():
    for x in range(-100,100):
        for y in range(-100,100):
            if x-y == 0:
                return True
    return False