x = input("Enter the sentence:-")
y =""
for char in x:
    if char not in y:
        y = y + char
print(y)