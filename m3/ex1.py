def valor_absoluto(x, y):    
    if x > y:
        dif = x - y
    else:
        dif = y - x
    return dif
    # ou então
    #    if x > y:
    #        return x - y
    #    else:
    #        return  y - x
        
print(valor_absoluto(7, 10))
print(valor_absoluto(10, 7))
print(valor_absoluto(100, 90))
print(valor_absoluto(90, 100))