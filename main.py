def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    
    print_report(text, book_path)
    


def print_report(text,path):
    print(f"-- Report of {path} --")
    print(f"{count_words(text)} words found in the document\n")
    
    sorted_list = sort_chars(text)
    for char in sorted_list:
        print(f"The {char["letter"]} character was found {char["num"]} times")
    print("--- END ---")


def sort_on(dict):
    return dict["num"]

def sort_chars(text):
    unsorted_chars = count_chars(text)
    sorted_list = []

    for c in unsorted_chars:
        if c.isalpha():
            entry = {
                "letter": c,
                "num": unsorted_chars[c]
            }
            sorted_list.append(entry)
    sorted_list.sort(reverse=True, key=sort_on)
   
    return sorted_list

def count_chars(text):
    chars = {}
    
    for char in text:
        letter = char.lower()
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars


def count_words(text):
    num_words = len(text.split())
    return num_words


def get_book(path):
    with open(path) as f:
        return f.read()
    

main()