def analyze_text(text):
    length = len(text)
    upper_text = text.upper()

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

    replaced_text = text.replace("helper", "assistant")
    print("Text with replacement:", replaced_text)

    print("Summary: this text has", length, "characters and", word_count, "words.")

    average_chars_per_word = length / word_count
    print("Average characters per word:", average_chars_per_word)

    average_words_per_page = word_count / (full_pages + 1)
    print("Average words per page:", average_words_per_page)


def short_summary(text):
    length = len(text)
    words = text.split()
    word_count = len(words)
    print("Short summary:", length, "chars and", word_count, "words.")


analyze_text("Hello, this is my first text helper test.")
analyze_text("I am building my own Python text helper project.")

short_summary("Hello, this is my first text helper test.")
short_summary("I am building my own Python text helper project.")