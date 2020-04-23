num = 40000000

while(True):
    if (num>1):
        for i in range (2,num):
            if (num % i)==0:
                break
            else:
                print("{} , ".format(num),end = "")
    num += 1
