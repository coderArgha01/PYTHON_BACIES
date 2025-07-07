

f=open("practice.txt","r")
data=f.read()
new_data=data.replace("argha","cat")
print(new_data)
f.close()
   
f=open("practice.txt","w")   
f.write(new_data)