# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character. It starts with 0 so character 5 is 4
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find ("c"))
# Advanced Slicing:
# Given the string
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# # Extract the name of the famous personality from the quote
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "

print(quote.find("John F. Kennedy"))
print(quote[83:-1])
# Manipulating Words:
# Given the string info
sentence = "Python is fun. Fun is good. Good is subjective. "
# a. Extract the word 'subjective' without knowing its exact position.
print(sentence.split("Python is fun. Fun is good. Good is,"))
# b. Extract every third word.
words = sentence.split()
every_third_word = words[::3]
result = ' '.join(every_third_word)
print(result)

# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(alphabet[0::6] + alphabet[6::9] + alphabet[9::13])
# Problem Set 3: String Methods
# Upper & Lower:
# # Convert the following text to lowercase: 
force = "MAY THE FORCE BE WITH YOU."
print(force.lower())
# # String Joining and Splitting:
# # Given the list
# # a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
joined_motto = " ".join(motto)
print(joined_motto)

# # b. Now, split the string at every occurrence of the letter 'a'.

print(joined_motto.split("a"))

# Replacing Words:
# Modify the 
sentence2 = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sentence2.replace("busy", "distracted"))
# b. Replace "plans" with "mistakes".
print(sentence2.replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
hello = "Iteration " * 7
print(hello)
# Word Search:
# Check if the word "moonlight" appears in the quote: 
quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote2.find("moonlight"))
print("moonlight" in quote2)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase:
phrase = "Supercalifragilisticexpialidocious"
print(len(phrase))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
pharse_list = phrase.count('i')
print(f'The letter "i" appears{pharse_list}')