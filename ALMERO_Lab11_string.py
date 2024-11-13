# 10 list of words, user input length of letters in word, display all words with that number of letters
words = []
length = []

for user in range(10):
    user = input("Enter a word: ")
    words.append(user)

letters = int(input("Enter desired number of letters to print: "))

for user in words:
    if len(user) == letters:
        length.append(user)
    else:
        continue     
print(f"The 10 words inputted include: {words}")
print(f"Words with {letters} letters: {length}")