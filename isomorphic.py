def isiso(str1,str2):
    size1 = len(str1)
    size2 = len(str2)
    
    #First_Check to check string' equal length

    if (size1 != size2):
        return False

    dic1 = {}
    dic2 = {}
    for x,y in zip(str1,str2):
        if x in dic1:
            if dic1[x] != y:
                return False
        else:
            dic1[x] = y

        #Reverse_order

        if y in dic2:
            if dic2[y] !=x:
                return False
        else:
            dic2[y] = x

    return True
        



str1 = 'egg'
str2 = 'addd'
op = isiso(str1,str2)
print(op)