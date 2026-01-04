def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    data={}
    for char in text:
        low = char.lower()
        if low in data :
            data[low] +=1
        else :
            data[low] = 1
    return(data)
def sorter(data):
    return dict(sorted(data.items(), key=lambda x:x[1], reverse=True))

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list