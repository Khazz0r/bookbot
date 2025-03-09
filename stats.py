import operator

def get_book_text(filepath) -> str:
    """Gets txt from a file in the file path given and returns a string of the file contents."""
    with open(filepath) as f:
        file_contents = f.read()
        return str(file_contents)

def get_num_of_words(text) -> int:
    """Gets the number of words from a string of text given."""
    split_words = text.split()
    return len(split_words)

def get_num_of_char(text) -> list:
    """Gets the number of each character from a string of text given and puts it into a dictionary with
    the key being the character and the value being the number of times that character was found."""
    dict_of_char = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        if char in dict_of_char:
            dict_of_char[char] += 1
        else:
            dict_of_char[char] = 1
    
    return dict_of_char
        
def sort_dict_of_char(dict):
    list_of_dict = []

    for key, value in dict.items():
        temp_dict = {"character": key, "num": value}
        list_of_dict.append(temp_dict)

    list_of_dict.sort(reverse=True, key=lambda x: x["num"])
    return list_of_dict
