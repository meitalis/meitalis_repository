from animals_parser import AnimalsParser

if __name__== '__main__':
    with open("zoo.txt") as fp:
        ap = AnimalsParser(fp)