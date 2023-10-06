sen = input("Enter the sentence:-")
Alpha = 'abcdefghijklmnopqrstuvwxyz'
for j in Alpha:
    if j not in sen.lower():
        print(f"The sentence :-{sen}","is not a pangram")
        break
else:
    print(f"The sentence:-{sen}"," is a pangram")

