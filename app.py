#reading of files 

def read_file():
    #open the file
    file = open('text.txt', 'r') #replace with the relative path of the file or the file itself if it's in the same direcory 

    #open the file 
    content = file.read()
    print(content)

    #close the file 
    file.close()

    return

def main():
    read_file()
    return 

if __name__ == "__main__":
    main()