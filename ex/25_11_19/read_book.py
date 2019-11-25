def read_book(file_path):
    file = open(file_path,"r+",encoding="utf-8")

    content = file.read()
    content_dic = {}
    print(content)
    new_content  = []

    #clean content
    for char in content:
        if char.isalpha() or char.isspace():
            new_content.append(char)

    # build dictionary to count words
    print(''.join(new_content),end="******\n")
    splitted = ''.join(new_content).split()
    for word in splitted:
        print(word)
        if not word.isspace():
            if content_dic.get(word.lower()):
                content_dic[word.lower()] += 1
            else:
                content_dic[word.lower()] = 1

    #file.write("".join(str(new_content)))
    #file.flush()
    file.close()

    print(content_dic)


if (__name__== '__main__'):
    file_path = r'C:\meital\ExperisDSCourse\ex\25_11_19\Shakespeare.txt'
    read_book(file_path)

