def search_tree(file_path):
    file = open(file_path, "r+", encoding="utf-8")

    (name_d,diameter) = (0,0)
    (name_h,height) = (0,0)
    for line in file:
        #print(line)
        if (line.startswith("#")):
            continue

        splitted_content = line.split('\t')
        #print(splitted_content)

        (name_d, diameter) = (splitted_content[0], float(splitted_content[2])) if diameter < float(splitted_content[2]) else (name_d, diameter)
        (name_h, height) = (splitted_content[0], float(splitted_content[3])) if height < float(splitted_content[3]) else (name_h, height)

    print("[max name,diameter,height]",  (name_h,height), (name_d,diameter))


    file.close()

if __name__== '__main__':
    file_path = r'C:\meital\ExperisDSCourse\ex\26_11_19\redwood-data.txt'
    search_tree(file_path)


