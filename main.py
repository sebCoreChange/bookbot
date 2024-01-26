"""
boot.dev training exercies
"""
def main():
    """
    main loop
    """
    book_path = r"books/frankenstein.txt"

    current_book = read_book(book_path)

    book_status( current_book, book_path )

def read_book(book_path):
    """
    Read book from set path.
    """
    with open( book_path , encoding="utf8") as f:
        return f.read()

def print_book(book):
    """
    Prints out the loaded book
    """
    print( book )

def get_book_size(book):
    """
    prints the word count of the book and returns the value as an int.
    """
    words = book.split()
    word_count = len( words )
    print( f"The book is { word_count } words long." )
    return word_count

def letter_counter(book):
    """
    Returns a dict with the char count of the book.
    """
    letter_dict = {}
    for letter in book.lower():
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] =1

    return letter_dict

def book_status( book, title ):
    """
    print out the info about the current book.
    """
    print( f"--- Begin report of {title} ---")
    get_book_size( book )
    letter_dict = letter_counter( book )
    letter_list = []
    for c in letter_dict:
        if c.isalpha():
            letter_list.append( (c , letter_dict[c] , ) )


    letter_list.sort(key=lambda tup: tup[1], reverse=True )
    for cup in letter_list:
        print( f"the '{cup[0]}' character was found {cup[1]} times" )
    print( f"--- End report ---")





if __name__ == '__main__':
    main()
