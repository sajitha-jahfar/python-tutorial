import re

#re.search(pattern, string)

# text = "Hello world"
# print(re.search(r"world", text))

# re.match(pattern, string)

# text = "Hello world"
# print(re.match(r"Hello", text))
# <re.Match object> → Found "Hello"
# print(re.match(r"world", text))
# None → "world" not at start

#3re.findall(pattern, string)
#eturns a list of all matches (not match objects).
# for extracting numbers, words, etc.
# text = "I have 2 apples and 5 oranges."
# print(re.findall(r"\d+", text))
# ['2', '5']
# text = "The price is 45 dollars, 30 cents, and 50 rupees."
# print(re.findall(r"\d+", text))
# ['45', '30', '50']

#  re.finditer(pattern, string)
# Returns an iterator of match objects.
# More powerful than findall (gives positions + details).

# text = "I have 2 apples and 5 oranges."
# for match in re.finditer(r"\d+", text):
#  print(match.group(), "at", match.start())
# 2 at 7
# 5 at 19

# re.sub(pattern, repl, string)
# Replaces all matches of the pattern with repl .
# Useful for cleaning or masking data.

# text = "Hello 123, welcome 456!"
# print(re.sub(r"\d+", "number", text))
# "Hello number, welcome number!"


#  re.split(pattern, string)
# Splits string wherever the pattern is found.
# Similar to str.split() but with regex power.

# text = "apple, orange; banana, grape"
# print(re.split(r"[;,]", text))
# ['apple', ' orange', ' banana', ' grape']

#  Grouping & Capturing
# text = "John: 34, Alice: 45, Bob: 23"
# print(re.findall(r"(\w+): (\d+)", text))
# [('John', '34'), ('Alice', '45'), ('Bob', '23')]

# Compiling Regex
# pattern = re.compile(r"\d+")
# text = "123 apples and 456 oranges"
# print(pattern.findall(text))
# ['123', ']


# # . Regex Flags
# # 1. re.IGNORECASE (or re.I )
# Makes the pattern case-insensitive.
# Matches regardless of upper/lower case.
# Regular Expressions 4
# import re
# text = "HELLO world"
# print(re.search(r"hello", text, re.IGNORECASE))
# <re.Match object> → Found "HELLO" (case ignored)

#  re.MULTILINE (or re.M )
# Treats each line as a separate string.
# ^ matches start of each line, and $ matches end
# text = """first line
# second line
# third line"""

# Find all lines starting with 's'
# print(re.findall(r"^s\w+", text, re.MULTILINE))
# ['second']
# Find all lines ending with 'e'
# print(re.findall(r"\w+e$", text, re.MULTILINE))
# ['line', 'line']
# re.DOTALL (or re.S )
# Makes the dot ( . ) match newline characters too.
# Without this, . matches everything except \n .
text = "Hello\nWorld"
# Normal dot (.) → won't cross newline
print(re.search(r"Hello.*World", text))
# None
# With DOTALL → dot matches newline too
print(re.search(r"Hello.*World", text, re.DOTALL))
# <re.Match object> → "Hello\nWorld"

# Real-Life Uses of Regular Expressions
# 1. Validation (Checking Input)
# Email addresses, phone numbers, PIN codes, passwords, etc.
import re
email = "user@example.com"
if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
 print("Valid email")
else:
 print("Invalid email")

# 2. Data Cleaning
#  Remove unwanted characters, spaces, or symbols.
text = "Price: $123.45"
print(re.sub(r"[^0-9.]", "", text))
# "123.45"

# 3. Text Extraction
#  Extracting dates, phone numbers, hashtags, mentions, etc.
tweet = "Excited for #Python3 and following @openai!"
print(re.findall(r"#\w+", tweet)) # ['#Python3']
print(re.findall(r"@\w+", tweet)) # ['@openai']

# 4. Search & Replace
#  Replace phone numbers with XXX , mask credit cards, etc
text = "Card: 1234-5678-9012-3456"
print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", text))