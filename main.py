def main():
    path = "books/frankenstein.txt"

    file = get_file_contents(path)
    
    wordCount = word_count(file)
    letterCount = letter_count(file)
    
    letterCountList = convert_dict_to_list(letterCount)
    letterCountList.sort(reverse=True, key=sort_on)
    
    print_report(path, wordCount, letterCountList)
    
def get_file_contents(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count(s):
    return len(s.split())

def letter_count(s):
    s = s.lower()
    chars = {}
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    list = []
    for key in dict.keys():
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})
    return list

def print_report(path, wordCount, letterCount):
    print("--- Begin report of", path, "---")
    print(wordCount, "words found in the document")
    print()
    for c in letterCount:
        print(f'The \'{c["char"]}\' character was found {c["num"]} times')
    
    print("--- End report ---")

main()
