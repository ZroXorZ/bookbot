def num_words(text):

    return len(text.split())

def sort_dict(text):
    char_counts = {}
    for i in text.lower():
        char_counts[i] = char_counts.get(i,0) + 1

    sorted_char_list = []
    for i, v in char_counts.items():
        sorted_char_list.append({'char': i, 'count': v})

    sorted_char_list.sort(key=lambda x: x['count'], reverse=True)

    return sorted_char_list