mynumber = []
for i in range(10):
    value = int(input())
    mynumber.append(value % 42)
print(len(set(mynumber)))
