word =input("enter a word")
print("\nHere's each letter in your word:")
for letter in word:
    print(letter)
print(len(word))
input("\n\nPress the enter key to exit.")

message = input("Enter a message: ")
new_message = ""
VOWELS ="aeiou"

for letter in message:
     if letter.lower() not in VOWELS:
         new_message += letter
         print("A new string has been created:", new_message)
         
print("\nYour message without vowels is:", new_message)
