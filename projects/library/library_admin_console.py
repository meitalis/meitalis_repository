import jsonpickle
from library import Library


def insert_author(library):
    first_name = input("insert first_name")
    last_name = input("insert last_name")
    id = input("insert id")

    library.insert_author(first_name,last_name,id)

def insert_book(library):

    author = input("choose author from list")
    last_name = input("insert book name")


    library.insert_book(first_name,last_name,id)

if __name__== '__main__':
    library = Library()

    commands = {
        '1': insert_author
    }

    cmd = -1
    while cmd != 0:
        cmd = input("1. insert author\n"
                    "2. insert book\n"
                    "3. serch book by name\n"
                    "4. search books by author\n"
                    "5. save books to file\n"
                    "6. show book list\n")


        print(cmd)
        commands.get(cmd,-1)(library)
    # book = Book("meital book",1)
    # serialized = jsonpickle.encode(book)
    # print(serialized)
    #
    # my_book = jsonpickle.decode(serialized)
    # my_book.print()
    # writers = {}
    #
    # writers_file_path = r'C:\meital\ExperisDSCourse\ex\27_11_19\writers.txt'
    # for writer in writers_file_path:
    #     if writer.startswith("#"):
    #         continue
    #
    #     writer_splitted = writer.split()
    #     writers[writer_splitted[0]] = (writer_splitted[1],writer_splitted[2])
    #     for i in range(len(writer_splitted)):
    #         if (i==0)
    #
    #
    #
    # file_path = r'C:\meital\ExperisDSCourse\ex\27_11_19\books.txt'
    # library_content = open(file_path)
