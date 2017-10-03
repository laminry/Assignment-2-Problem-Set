finput = input("Enter Name : \n")
cname = finput.replace("-", " ")
name = ""
for i in cname.upper().split():
    name += i[0]
print(name)
