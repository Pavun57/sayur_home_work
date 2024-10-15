def clean_report(paragraph):
    words = paragraph.split()  # Split the paragraph into words
    word_count = {}  # Dictionary to store word counts and their indices

    # List of words to exclude from counting
    exceptions = {"the", "is", "a", "good"}

    for i, word in enumerate(words):
        clean_word = word.strip('.,!?"').lower()  # Clean up punctuation and handle case sensitivity

        # Skip the word if it's in the exception list
        if clean_word in exceptions:
            continue

        if clean_word not in word_count:
            word_count[clean_word] = {'count': 1, 'indices': [i]}
        else:
            word_count[clean_word]['count'] += 1
            word_count[clean_word]['indices'].append(i)

    # Now print the results
    for word, info in word_count.items():
        if info['count'] >= 3:
            print(f"'{word}' is repeated {info['count']} times at indices: {info['indices']}")
        else:
            print(f"{word} is unques")

# Input from the user
paragraph = input("Enter the paragraph: ")
clean_report(paragraph)
