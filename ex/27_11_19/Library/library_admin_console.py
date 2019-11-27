from book import Book
from writer import Writer

if __name__== '__main__':
    writers = {}

    writers_file_path = r'C:\meital\ExperisDSCourse\ex\27_11_19\writers.txt'
    for writer in writers_file_path:
        if (writer.startswith("#")):
            continue

        writer_splitted = writer.split()
        writers[writer_splitted[0]] = (writer_splitted[1],writer_splitted[2])
        for i in range(len(writer_splitted)):
            if (i==0)



    file_path = r'C:\meital\ExperisDSCourse\ex\27_11_19\books.txt'
    library_content = open(file_path)
