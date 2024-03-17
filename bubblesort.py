l = []
a = int(input("Enter no of elements you want to insert: "))
i = 0
while i<a:
    b = int(input("Enter the number of elements: "))
    l.append(b)
    i+=1
    
print(f"the list is {l}")

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
    print(l)