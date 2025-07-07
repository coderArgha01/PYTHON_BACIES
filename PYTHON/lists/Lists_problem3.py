
#Check if a list contain a palindrom of elements

list =[1,2,3,2,1]

list_copy=list.copy()

list_copy.reverse()

if(list_copy==list):
    print("palindrom")
else:
    print("not palindrom")
