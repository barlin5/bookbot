#getting the word count in each book
def get_num_words(text):
    return len(text. split())

#getting text from the book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#getting char count for every word in book
def get_num_char(text):
#   print(text)
    d = {}
    for i in text:
        if i.lower() not in d:
            count = 0
            for char in text:
                if char.lower() == i.lower():
                    count +=1
            d[i.lower()] = count
    return d            

def sort_dict(num_chars):
    l = []
    alpha_list = []
    for k,v in num_chars.items():
        l.append({"char":k, "count":v})
    l.sort(key=sort_on, reverse=True)
    for i in l:
        if i['char'].isalpha():
            alpha_list.append(i)
    return alpha_list
def sort_on(num_chars):
    return num_chars["count"]


