from stats import get_num_of_words, get_book_text, get_num_of_char, sort_dict_of_char

def main():
    file_path = "books/frankenstein.txt"


    num_of_words = get_num_of_words(get_book_text(file_path))
    num_of_char_dict = get_num_of_char(get_book_text(file_path))
    sorted_char_list = sort_dict_of_char(num_of_char_dict)


    print(
f'''
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_of_words} total words
--------- Character Count -------'''
    )

    # Dynamically print out characters from sorted list of dictionaries into final output for bookbot no matter what it finds
    valid_char = []
    for char_dict in sorted_char_list:
        if char_dict["character"].isalpha():
            valid_char.append(f"{char_dict['character']}: {char_dict['num']}")
    
    print("\n".join(valid_char))

    print(
"============= END ==============="
    )

main()
