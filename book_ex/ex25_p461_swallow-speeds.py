def get_average(file_path):
    file = open(file_path, "r+", encoding="utf-8")

    num = 0
    sum_all = 0
    counter = 0

    for line in file:
        #print(line)
        try:
            num = float(line)
            sum_all += num
        except ValueError as e:

            e.__traceback__.p
            print("Handle ValueError")
            if (line.startswith("#") or line.isspace()):
                print("line startswith # or space skip it")
                continue

            num = float(line.replace("#",''))
        finally:
            counter += 1
            sum_all += num
            print("sum_all",sum_all)
            print("average", sum_all/counter)

    file.close()

if __name__== '__main__':
    file_path = r'C:\meital\ExperisDSCourse\ex\26_11_19\swallow-speeds.txt'
    get_average(file_path)


