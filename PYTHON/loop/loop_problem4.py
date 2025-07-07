

#print the elements of the following list using a loop:
#   [1,4,9,16,25,36,49,64,81,100]



val =(1,4,9,16,25,36,49,64,81,100)

num =0
while num <=len(val):
    if(val[num] == 25):
       num +=1
       continue
    print(val[num])
    num +=1


'''for num in val:
    if(num == 16):
        continue
    print(num)'''   