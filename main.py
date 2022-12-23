import sys, datetime
a= sys.stdin.readline()
b=a.split(" - ")
Book_info=0
Book_name=0
Writer=0
Added_in=datetime.datetime.today().strftime("%d %B %Y")

for i in b:
    Book_info+=1


if Book_info!=2 :
    print("Wrong input")
elif b[1]=="":
    print("Wrong input")
else:
    print(f"Book name: {b[0]} \nWriter: {b[1]}" f"Added in: {Added_in}")