import re

def clear():
    str = "1234 56790ab cdefA BCDE?F!@#$%^&*()_+<>?,./"
    result = re.sub(r'[^a-zA-Z0-9 ]', "", str)
    print (result)

def read_from_file(file_path):
    file = open(file_path,"r+",encoding="utf-8")
    file_content = file.read()
    file.close()

    return file_content


def clear_unused_chars(content):
    clean_content = []

    for char in content:
        if char.isalpha() or char.isspace():
            clean_content.append(char)
        else:
            clean_content.append(" ")
    return  clean_content


def count_words(file_path):

    content = read_from_file(file_path)

    clean_content = clear_unused_chars(content)

    content_dic = {}
    (max_word_rep, max_repetition) = (0,0)

    splitted_clean_content = ''.join(clean_content).split()
    print(splitted_clean_content)
    for word in splitted_clean_content:
        if not word.isspace():
            if content_dic.get(word.lower()):
                content_dic[word.lower()] += 1
            else:
                content_dic[word.lower()] = 1

            (max_word_rep, max_repetition) = (word.lower(), content_dic[word.lower()]) if max_repetition < content_dic[word.lower()] else (max_word_rep, max_repetition)

    print(content_dic)
    return (max_word_rep, max_repetition)


if __name__== '__main__':
    file_path = r'C:\meital\ExperisDSCourse\ex\25_11_19\test_file.txt'
    max_word_rep, max_repetition =  count_words(file_path)
    print(max_word_rep,max_repetition)

    #test regex
    clear()
