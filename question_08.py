#mehtod 1
x =input("enter the sentence:-")
word= input("Enter the word:-")
if word in x:
    print("The number of times word in the sentence:-",x.count(word))



#method 2
x =input("enter the sentence:-")
word= input("Enter the word:-")
lst = (x.split())
count= 0
for x in lst:
    if x == word:
       count+=1
print(count)
