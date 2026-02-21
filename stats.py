def sort_on(array):
    return array['num']
def number_of_word(book_text) :
    words_in_book = book_text.split()
    number_of_word = len(words_in_book)
    return number_of_word 

def number_of_characters(book_text) :
    count_laters = {}
    words_in_book = book_text.split()
    for word in words_in_book : 
        for char in list(word.lower()):
            if char in count_laters :
                count_laters[char] += 1
            else : 
                count_laters[char] = 1 

    return count_laters

def dirctory_to_array(count_laters):
    latters_array = []
    for char in count_laters :
        if char.isalpha() :
            latters_array.append({"char": char, "num": count_laters[char] })
    latters_array.sort(reverse=True,key=sort_on)
    return latters_array
