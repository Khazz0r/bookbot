from stats import get_num_of_words, get_book_text, get_num_of_char, sort_dict_of_char
import sys

def main():
    #Ensure correct number of arguments are passed into the command
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print(
'''
Please put in only the script and absolute or relative file path for the bot, example:

"python3 main.py books/frankenstein.txt"
'''
        )
        sys.exit(1)

    else:
        num_of_words = get_num_of_words(get_book_text(sys.argv[1]))
        num_of_char_dict = get_num_of_char(get_book_text(sys.argv[1]))
        sorted_char_list = sort_dict_of_char(num_of_char_dict)
        print(
f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
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
