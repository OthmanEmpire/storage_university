def func(x,y):
    if(y == 0):
        return 0
    else:
        print(x,y)
        return x + func(x,y-1)

func(10,10)
