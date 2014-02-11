x=[10,5,6,74,1,3,2,63,9,45]
for i in range(1,len(x)-1):
    for j in range(i,-1,-1):
        if(x[j]>x[j+1]):
            temp = x[j+1]
            x[j+1] = x[j]
            x[j] = temp
        print x
