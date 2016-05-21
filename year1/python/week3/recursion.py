def sumListRec(a):
    if(len(a) == 0):
        return 0
    else:
        return a[0] + sumListRec(a[1:])


a = 'Banana'

b = sumListRec(a)
print(b)
