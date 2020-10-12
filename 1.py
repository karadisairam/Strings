s=input("enter the string :")
i=0
for x in s:
    print("The char present +ve index {} and at -ve index is {}".format(i,i-len(s),x))
    i=i+1