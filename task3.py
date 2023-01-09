import sys, datetime, os

from os.path import exists

if not exists("book_list.txt"):
        open("book_list.txt", "x")

command = sys.argv

class Book:

    def set_id(self):
        with open("book_list.txt", "r+") as f:
            obj = f.readlines()
            id=1
            if obj:
                id=int(obj[-5].split(":")[1]) + 1
            element=(f'Book ID: {id}')
            f.write(f"{element}\n")
        return True
        
    def add_book(self):
        title = input("Enter book name:\n")
        author = input("\nEnter writer name:\n")
        with open("book_list.txt", "a+") as f:
            element=(f'Book name: {title}\nWriter: {author}')
            f.write(f"{element}\n")
            print("\nAdded succesfully!")
        return True
        
    def set_date(self):
        with open("book_list.txt", "a+") as f:
            obj = f.readlines()
            element = (f'Added in: {datetime.datetime.today().strftime("%d %B %Y")}')
            f.write(f"{element}\n{'*' * 50}\n")

    def show_book(self):
        book_id=input("Enter book ID:\n")
        print(f"\n{'*'*50}")
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
    
    def show_all(self):
        with open("book_list.txt", "r+") as f:
            obj = f.readlines()
            for i in range(0, len(obj), 5):
                search = obj[-5].split(":")[1].strip()
                count=0
                if count < int(search):
                    count=search
        print(f"There are {count} books!")
        print(f"{'*'*50}")
        print(*obj)

    def remove_book(self):
        book_id = input("Enter book ID:\n")
        with open("book_list.txt", "r+") as f:
                obj = f.readlines()
                f.seek(0)
                for i in range(0, len(obj), 5):
                    remove_element = obj[i].split(":")[1].strip()
                    if book_id == remove_element:
                        index = i
                        f.truncate()
                        for i in range(len(obj)):
                            if i not in  range(index, index+5):
                                f.write(obj[i])
                        print('\nSuccesfully deleted!\n')
                        break
                else:
                    print('\nID not found\n')

book = Book()
if len(command) == 2 and command[1] == 'add':
    book.set_id()
    book.add_book()
    book.set_date()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'all':
    book.show_all()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'book':
    book. show_book()
elif len(command) == 2 and command[1] == 'remove':
    book.remove_book()
else:
    print('Please, enter right input')