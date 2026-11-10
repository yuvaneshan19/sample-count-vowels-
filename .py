A= input("Enter a word:")
count = 0
for i in A:
    if i in "aeiou":
        count+=1
print('Number of vowels:',count)