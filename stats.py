def count_words(path_to_file):
    with open(path_to_file) as f:
        string = f.read()
    word_list = string.split()
    words_number = len(word_list)
    message = f"Found {words_number} total words"
    return print(message)

def count_chars(path_to_file):
    with open(path_to_file) as f:
        book = f.read()
        book_lowercase = book.lower()
    set_of_chars = set(book_lowercase)
    mylist = []
    for chars in set_of_chars:
        mydictionary = {}
        mydictionary["char"] = chars
        mydictionary["number"] = book_lowercase.count(chars)
        mylist.append(mydictionary)
    def sort_on(items):
        return items["number"]
    mylist.sort(reverse=True, key=sort_on)
    for item in mylist:
        print(f"{item["char"]}: {item["number"]}")
