def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def get_each_char(text):
    text = text.lower()
    result = {}
    for i in range(0, len(text)):
        if text[i] not in result:
            result[text[i]] = 1
        else:
            result[text[i]] += 1
    return result
