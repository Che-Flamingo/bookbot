def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    wordcount = count_words(text)
    create_report(wordcount, count_chars(text), bookpath)

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def create_report(word_count, char_count, book):
    char_count_list = []
    for k,v in char_count.items():
        char_count_list.append({"letter":k, "num":v})
    char_count_list.sort(reverse=True, key=sort_on)
    

    print(f"--- Begin report of {book} ---")
    print(f"{str(word_count)} words was found in the document \n")
    for item in char_count_list:
        if item['letter'].isalpha():
            print(f"The '{item['letter']}' character was found {item['num']} times")
    print(f"--- End Report ---")
    
def count_chars(text):
    text = text.lower()
    char_occurence = {}
    for i in range(0,len(text)):
        if text[i] in char_occurence:
            char_occurence[text[i]] += 1
        else:
            char_occurence[text[i]] = 1
    return char_occurence

def sort_on(dict):
    return dict["num"]


main()