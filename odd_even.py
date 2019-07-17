def showNumbers (limit):
    c = -1
    i = 0
    while limit >= 0:
        if limit % 2 ==0:
            c = c+1
            print(str(c)+" ODD")
            limit = limit-1
        else:
            c = c + 1
            print(str(c)+" EVEN")
            limit = limit -1


someNumber = int(input("Says the limit: "))
showNumbers(someNumber)
