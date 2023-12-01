from search import Search

def perform_search(lib):
    path="tbr_books.txt"
    libraries=lib
    available=Search(path, libraries).check_availability()
    if len(available)<=0:
        available=None
    return available

def main():
    avb=[]
    print("HELMET CHECK\nEnter command:\n")
    cmd=int(input("1 - General availability\n2 - Choose libraries\n3 - Exit\n"))
    if cmd==1:
        avb=perform_search([])
    elif cmd==2:
        options=["", "Oodi", "Kannelmäki", "Rikhardinkatu"]
        lib=[]
        while True:
            print(f"Searching from {lib}")
            opt=int(input("1 - Oodi\n2 - Kannelmäki\n3 - Rikhardinkatu\n4 - Custom\n5 - Done\n"))
            if opt in (1,2,3):
                if options[opt] not in lib:
                    lib.append(options[opt])
            elif opt==4:
                new=input("Enter the name of the library: ")
                if new not in lib:
                    lib.append(new)
            elif opt==5:
                break
        avb=perform_search(lib)
    elif cmd==3:
        return
    print("The following books are available:\n")
    for link in avb:
        print(link)

if __name__=="__main__":
    main()
