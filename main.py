def main():
    import sys
    from stats import count_words
    from stats import count_chars
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at $path_to_file ...")
    print("----------- Word Count ----------")
    count_words(path_to_file)
    print("--------- Character Count -------")
    count_chars(path_to_file)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        print(f.read())



main()