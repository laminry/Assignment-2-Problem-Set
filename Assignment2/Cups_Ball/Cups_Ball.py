number = [1,0,0]
word = input("Enter Word").upper()
la = "A"
lb = "B"
lc = "C"
def myswap1():
    global a,b
    a = number.pop(1)
    b = number.pop(0)
    number.insert(0,a)
    number.insert(1,b)
def myswap2():
    global b,a
    a = number.pop(2)
    b = number.pop(1)
    number.insert(1,a)
    number.insert(2,b)
def myswap3():
    global a , b
    a = number.pop(2)
    b = number.pop(0)
    number.insert(0,a)
    number.insert(2,b)

for i in range(0, len(word)):
    if word[i]==la:
        myswap1()
    elif word[i]==lb:
        myswap2()
    elif word[i]==lc:
        myswap3()
print(number)
