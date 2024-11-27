with open("books/frankenstein.txt", "r") as file:
    content = file.read()  # Read all file content into a string
    words = content.split()  # Split the content by whitespace into words
    print(len(words))  

def count_characters(text):
    # Initialize an empty dictionary for character counts
    char_count = {}

    # Convert the text to lowercase to ensure case insensitivity
    text = text.lower()

    # Loop through each character in the text
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            # Update the dictionary with character counts
            char_count[char] = char_count.get(char, 0) + 1

    # Return the dictionary of character counts
    return char_count

def convert_and_sort(character_counts):
    # Convert the dictionary into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in character_counts.items()]

    # Sort the list by the "num" key in descending order
    char_list.sort(reverse=True, key=lambda x: x["num"])

    # Return the sorted list
    return char_list
