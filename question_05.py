Sentence = input("Enter the pragraph:-")
count , digit, special , upper , lower  = 0 , 0 , 0 , 0 , 0
for i in Sentence:
    if (i.isupper()):
        upper+=1
    elif (i.islower()):
        lower+=1
    elif (i.isdigit()):
        digit+=1
    elif (i.isalpha()):
        count+=1
    else:
        special+=1


print(upper, "Total upper case letter:-")
print(lower, "Total lower case letter:-")
print(digit, "Total digit in paragraph:- ")
print(count, " Total alphabet in the paragraph:-")
print(special, " Total special case:-")