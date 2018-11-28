the_quote = input("enter a 1 sentence quote, non-alpha separate words: ")
word = ""

for letter in the_quote:
    if letter.isalpha():
        word += letter
    elif word.lower() >= "h":
        print(word.upper())
        word = ""
    else:
        word = ""
    
if word.lower() >= "h":
        print(word.upper())
