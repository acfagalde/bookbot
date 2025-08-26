def word_count(file_contents):
    words = file_contents.split()
    total_words= len(words)
    print(f"Found {total_words} total words")

def sort_on(items):
    return items["key"]

def letter_count(file_contents):
    file_contents = file_contents.lower()
    letter_dic = {}
    for item in file_contents:
        letters = item.split()
        for letter in letters:
            letter_dic[letter] = letter_dic.get(letter, 0)+1
    list_of_dicts = [{key: value} for key, value in letter_dic.items()]
    list_of_dicts.sort(key=lambda d: list(d.values())[0], reverse=True)
    for item in list_of_dicts:
        for key, value in item.items():
            print(f"{key}: {value}")