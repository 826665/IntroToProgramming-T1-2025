Sentence1 = input("Enter a Sentence\n>")



print(Sentence1.upper())
print(Sentence1.strip())
print(Sentence1.replace("bad", "good"))

if Sentence1.endswith("."):
    print(True)
else:
    print (False)