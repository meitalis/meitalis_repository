def compute(n):
    for i in range(1,5):
        a = n ** i
        yield a


def compute_all():
    for i in range(1,1001):
        ans_all = compute(i)
        yield ans_all


def write_to_file(file_path):
    f = open(file_path,"a+",encoding="utf-8")

    for g in compute_all():
        print(*(i for i in g),sep=", " ,file=f)
        
    f.close()

if (__name__== '__main__'):
    file_path = r'C:\meital\ExperisDSCourse\ex\26_11_19\test_file.txt'
    write_to_file(file_path)

    # Then read the numbers from the file powers.txt and print a list of the cubes of all the
    # numbers between 1 and 100
    # f = open(file_path)
    # lst = [line.split(',')[2] for line in f]
    #print(lst)

