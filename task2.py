import sys, datetime, os

from os.path import exists

if not exists("book_list.txt"):
    open("book_list.txt", "x")

command = sys.argv

def add_book():
    title = input("Enter book name:\n")
    author = input("\nEnter writer name:\n")
    with open("book_list.txt", "r+") as f:
        obj = f.readlines()
        id=1
        if obj:
            id=int(obj[-5].split(":")[1])+1
        element=(f'Book ID: {id}\nBook name: {title}\nWriter: {author}\nAdded in: {datetime.datetime.today().strftime("%d %B %Y")}\n')
        f.write(f"{element}{'*' * 50}\n")
        print("\nAdded succesfully!")

def show_book():
    book_id=input("Enter book ID:\n")
    with open("book_list.txt", "r+") as f:
        obj = f.readlines()
        for i in range(0, len(obj), 5):
            search = obj[i].split(":")[1].strip()
            if book_id == search:
                index=[i, i+1, i+2, i+3, i+4]
                for i in range(len(obj)):
                    if i in index:
                        print(obj[i])
                break


def show_all():
    with open("book_list.txt", "r") as f:
        obj = f.readlines()
        for i in range(0, len(obj), 5):
            search = obj[-5].split(":")[1].strip()
            count=0
            if count < int(search):
                count=search
        print(f"There are {count} books!")
        print(*obj)

def remove_book():
   book_id = input("Enter book ID:\n")
   with open("book_list.txt", "r+") as f:
        obj = f.readlines()
        f.seek(0)
        index=-1
        for i in range(0, len(obj), 5):
            remove_element = obj[i].split(":")[1].strip()
            if book_id == remove_element:
                index = i
                range_list = [index, index + 1, index + 2, index + 3, index + 4]
                f.truncate()
                for i in range(len(obj)):
                    if i not in  range_list:
                          f.write(obj[i])
                print('\nSuccesfully deleted!\n')
                break
            else:
                print('\nID not found\n')
            if index != -1:
                number_list = [index, index + 1, index + 2, index + 3, index + 4]
                f.truncate()
                for i in range(len(obj)):
                    if i not in number_list:
                        f.write(obj[i])
                print('\nBook was deleted...\n')



if "add" in command:
    add_book()

elif "show" and "book" in command:
    show_book()

elif "show" and "all" in command:
    show_all()

elif "remove" and "book" in command:
    remove_book()