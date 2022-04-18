""" Strings are another data types that consists of characters """

""" Quotation """
# single-quote
message = '1.) Hello World \n'  # string with single-quote that is only for one line
message += '2.) Bobby\'s World \n'  # single-quote with escape sequence
message += '3.) "Bobby\'s World" \n'  # double-quote inside of single-quote w/ escape sequence

# double-quote
message += "4.) Bobby's World \n"  # single-quote inside of double-quote
message += "5.) One wise man said \"Time is Gold\". \n"  # double-quote with escape sequence
message += "6.) One wise man said 'Time is Gold'. \n"  # single-quote inside of double-quote w/o escape sequence

# inline-quote
message += """7.) Bobby's World was a good
    cartoon in the 1990s. """  # inline-quote with multiple lines

print(message)

""" Concatenation """
firstName = "Frederick"
lastName = "Castaneda"
fullName = firstName + " " + lastName
print("8.) Your full name is " + fullName)

""" Formatted String """
name = "Fred"
course = "Computer Science"
greeting = "Hello! Name: {} Course: {}".format(name, course)
print("9.) " + greeting)

""" Array of a string """
array = "Happy Birthday"
print("10.) The letter from index 0 is: ", array[0])  # index
print("11.) Print only the second word: ", array[6:14])  # slicing index
print("12.) Print only the first word: ", array[:5])  # no need to indicate the initial point if it's 0
print("13.) Print only the last 3 letters word: ", array[11:])  # no need to indicate the last point if it's up to end
print("14.) Print all words: ", array[:])  # no need to indicate initial and last point to print all

""" Methods/function of string """
# len() function
greetings = "Hello World"
print("15.) The length of Hello World is: ", len(greetings))  # to return the length of the strings

# upper() method, lower() method and title() method
phrase = "Programming is love"
print("16.) " + phrase.lower())  # all lowercase
print("17.) " + phrase.upper())  # all uppercase
print("18.) " + phrase.title())  # capitalize the first letter of the word

# count() method
word = "Programming"
print("19.) Letter 'M' repeats", word.count("m"), "counts")  # to count how many characters appear in a string
print("20.) Word 'Pro' repeats", word.count("Pro"), "count")  # to count how many word appear in a string

# find() method
hunt = "Looking?"
print("21.) What position did letter 'n' starts in a word 'looking'?:", hunt.find("n"))  # finds the position of the letter
print("22.) What position did 'king' starts in a word 'looking'?:", hunt.find("king"))  # finds the position of the word

# replace() method
replacementWord = "Frederick Castaneda"
newWord = replacementWord.replace("Castaneda", "Padilla")  # first, word you want to replace. second, the replacement
print("23.) New word replacement with changed variable: " + newWord)

replacementWord = replacementWord.replace("Frederick", "Daniel")  # with the same variable
print("24.) New word replacement with same variable: " + replacementWord)

# strip() method
print("25.) " + replacementWord.strip("neda"))  # remove what's on the parameter

# split() method
print("26.) To make it a list.".split())  # to make it a list
print("27.) To-remove-characters-from-the-string".split("-"))  # removes all characters from strings
