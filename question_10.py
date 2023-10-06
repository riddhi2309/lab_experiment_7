sen = input("Enter the string with the hyphen:-")
lst = (sen.split('-'))
for i in range(0,len(lst)):
    min = i
    for j in range(i,len(lst)):
        if i!=j:
           if lst[j]<lst[min]:
               min = j
    lst[i],lst[min] = lst[min],lst[i]
print(lst)
str1 = '-'.join(lst)
print(str1)