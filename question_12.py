n =int(input("Enter the number"))
line = '+'+(('/'+ '\\')*n)+"+"
print(line)
for i in range(n):
    print(("|"+(n*2*" ")+"|"),end="\n")
print(line)