def count_words(text):
    """
    Function to count the number of words in a given text.

    Args:
    text (str): The input text to count words from.

    Returns:
    int: The number of words in the text.
    """
    # Split the text into words using whitespace as delimiter
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    # Prompt the user to enter a sentence or paragraph
    input_text = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if not input_text.strip():
        print("Error: Input is empty.")
    else:
        # Count the number of words
        num_words = count_words(input_text)
        # Display the word count
        print("Word count:", num_words)

if __name__ == "__main__":
    main()
