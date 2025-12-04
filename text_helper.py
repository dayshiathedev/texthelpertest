text = "Hello, this is my first text helper test."

length = len(text)
upper_text = text.upper()

# New: split the text into words
words = text.split()
word_count = len(words)

print("Original text:", text)
print("Length of text:", length)
print("Uppercase version:", upper_text)
print("Words list:", words)
print("Number of words:", word_count)

chars_per_page = 200

full_pages = length // chars_per_page
extra_chars = length % chars_per_page

print("Full pages (200 chars each):", full_pages)
print("Remaining characters on last page:", extra_chars)

# Replace a word in the text
replaced_text = text.replace("helper", "assistant")
print("Text with replacement:", replaced_text)

print("Summary: this text has", length, "characters and", word_count, "words.")