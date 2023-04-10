# 1) write a function that displays the string "Hello World!" on the console

# 2) write a function that takes a string as a parameter and displays it on the console

# 3) write a function that takes a name (type string) as parameter and returns the following string
#    "Hi there, <name>!". hint: google f"{}" in python

# 4) write a function that takes a full name as a parameter and displays it on the console
#    the same name 3 times: first time in uppercase, second time in lowercase and third time only initial letters
#    with capital letters. Example: input: "gregorio canepa". output: GREGORIO CANEPA, gregorio canepa, Gregorio Canepa

# 5) write a function that takes two parameter: first parameter: a random sentence, second parameter: a single word.
#    The function should return true if the word in the second parameter exists in the sentence from the first parameter.
#    Example: "I drink mate all the time." "coffee". Output: False


# 6) Write a Python program to check whether a string starts with specified characters. 
# Example: main_string = "Java is the worst." substring = "Python".
# Expected output: False

def check_string (main, substring):
    if substring in main:
        return True
    else:
        return False
    
print(check_string('Java is the worst.', 'Python' ))



# 7) Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample list: ["this", "exercise", "is", "quite", "easy"] 
# Expected output: 'Longest word: "exercise". Length of the longest word: 9'

def longest_word (list):
    longest = ''
    for word in list:
        if (len(word) > len(longest)):
            longest = word
    return longest

lista  = ['pepe', 'mundo', 'toto', 'el_mono', 'azucar']
palabra = longest_word(lista)
print (palabra)

# 8) Exercise 5 2.0: Write a function that takes two parameters: 
# first parameter: a random sentence, second parameter: a single word.
# The function should return true if the word in the second parameter exists in the sentence from the first parameter.
# You can't use "if word in sentence" sintax.
# Example: "I drink mate all the time." "coffee". Output: False.
def two_strign(sentence, word):
    sentence_words = sentence.split() 
    for sentence_word in sentence_words:
        if sentence_word == word:
            return True
    return False
# 9) Write a Python program to count occurrences of a substring in a string.
# main_string = "Python is a great language. Python can be used for web development and data science.
#               It's name comes from the british comedy group Monty Python."
# substring = "Python"

def count_string(main_string, substring):
    words = main_string.split() 
    count_strign = 0
    for sentence_word in words:
        if sentence_word == substring:
            count_strign += 1
    return count_strign

main_string = "Python is a great language. Python can be used for web development and data science. It's name comes from the british comedy group Monty Python."
substring = "Python"
count = count_string(main_string, substring)
print(f"The substring '{substring}' appears {count} times in the string.")


# 10) Write a python program that replaces commas "," with dots "." and dots with commas.
# original_string = "In some countries people write decimals like this: 3.14, whereas other write it this way 3,14."
# expected output: "In some countries people write decimals like this: 3,14. whereas other write it this way 3.14,"

original_string = "In some countries people write decimals like this: 3.14, whereas other write it this way 3,14."
char_dot = "."
char_comma = ","
expected_output =""

for char in original_string:
    if char == char_dot:
        expected_output += char_comma
    elif char == char_comma:
        expected_output += char_dot
    else:
        expected_output += char
print (expected_output)