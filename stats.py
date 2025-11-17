from utils import get_book_text
import sys

def count(file_contents):
    list = file_contents.split()
    words = len(list)
    return f"Found {words} total words"

def characters(file_contents):
    dict_char = {}
    lowercase = file_contents.lower()
    list_lowercase = lowercase.split()
    for i in range(0, len(list_lowercase)):
        word = list_lowercase[i]
        for j in range(0, len(word)):
            letter = word[j]
            
            if not letter.isalpha():
                continue
            
            if letter not in dict_char:
                dict_char[letter] = 1
            else:
                dict_char[letter] = dict_char[letter] +  1
    return dict_char

def sort(dict_char):
    return dict_char["count"]

def sorting(filepath):
    text = get_book_text(filepath)
    dict_char = characters(text)

    list_char_in_dict = []
    for letter, count in dict_char.items():
        list_char_in_dict.append({"letter": letter, "count": count})
    
    list_char_in_dict.sort(reverse = True, key=sort)
    for item in list_char_in_dict:
        print(f"{item['letter']}: {item['count']}")