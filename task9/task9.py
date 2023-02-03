import sys, datetime, os

from os.path import exists

import pymysql.cursors
connection = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "12345",
                             db = "project",
                             charset = "utf8mb4",
                             cursorclass = pymysql.cursors.DictCursor)

command = sys.argv


def create_table():
    with connection.cursor() as cursor:
        sql = """
        create table if not exists Book_info(
        Book_id int not null auto_increment primary key,
        Book_name varchar(255) not null,
        Writer varchar(255) not null,
        Added_in date not null,
        Exist boolean not null, 
        Price integer not null
        ) 
        """
        cursor.execute(sql)
    connection.commit()

def create_book():
    with connection.cursor() as cursor:
        Book_name = input("Enter book name:\n")
        Writer = input("\nEnter writer name:\n")
        Added_in = datetime.datetime.today()
        Price = int(input("\nEnter price of book:\n"))
        Exist = input("\nEnter current existence of book:\n")
        sql = """
        insert into Book_info(Book_name, Writer, Added_in, Price, Exist) values(%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, ({Book_name}, {Writer}, {Added_in}, {Price}, {Exist}))
    connection.commit()

def show_all():
    with connection.cursor() as cursor:
        sql = """
        select * from Book_info
        """
        cursor.execute(sql)
        results = cursor.fetchall()
    for i in results:
        print(i)

def show_book():
    with connection.cursor() as cursor:
        id = int(input("Enter Book_id:\n"))
        sql = f"""
        select * from Book_info where Book_id = {id}
        """
        cursor.execute(sql)
        Result = cursor.fetchone()
        print(Result)


def change_status():
    with connection.cursor() as cursor:
        id = int(input("Enter Book_id:\n"))
        sql = f"""
            update Book_info 
                set Exist = Case
                    when Exist = True then False
                    when Exist = False then True

                End
                    where Book_id = {id}
        """
        cursor.execute(sql)
    connection.commit()

def change_price():
    with connection.cursor() as cursor:
        id = int(input("Enter Book_id:\n"))
        new_price = input("\nEnter new price of book:\n")
        sql =f"""
        update Book_info set price = {new_price} where Book_id = {id}
        """
        cursor.execute(sql)
    connection.commit()

def remove_book():
    with connection.cursor() as cursor:
        id = int(input("Enter Book_id:\n"))
        sql = f"""
        delete from Book_info where Book_id = {id}
        """
        cursor.execute(sql)
    connection.commit()

def search_book():
    with connection.cursor() as cursor:
        Search_word = input("Enter word:\n")
        sql = f"""
        select * from Book_info where Book_name like "%{Search_word}%" or Writer like "%{Search_word}%"
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

if len(command) == 3 and command[1] == 'add' and command[2] == 'table':
    create_table()

elif len(command) == 3 and command[1] == 'add' and command[2] == 'book':
    create_book()

elif len(command) == 3 and command[1] == 'show' and command[2] == 'all':
    show_all()

elif len(command) == 3 and command[1] == 'show' and command[2] == 'book':
    show_book()

elif len(command) == 3 and command[1] == 'change' and command[2] == 'status':
    change_status()

elif len(command) == 3 and command[1] == 'change' and command[2] == 'price':
    change_price()

elif len(command) == 2 and command[1] == 'remove':
    remove_book()

elif len(command) == 2 and command[1] == 'search':
    search_book()