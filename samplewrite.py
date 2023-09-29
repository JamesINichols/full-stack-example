def write_file():
    print("Writing a file..")
    try:
        f = open("my_file.txt", "w")
        for num in range(5):
            f.write("Line " + str(num) + "\n")
        f.close()
    except Exception:
        print("Could not write to file")


def read_file():
    print("Now reading the file..")
    try:
        f = open("my_file.txt", "r")
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print("Could not read to file")

def main():
    write_file()

    read_file()

if(__name__=="__main__"):
    main()
