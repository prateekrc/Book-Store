import mysql.connector
from datetime import datetime
now = datetime.now()



try:
    connect = mysql.connector.connect(host="localhost", username="root", password="root", database="test")
    cursor = connect.cursor()
    print("connected")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

ch2, adm = 0, 0

try:
    chr1 = int(input("Enter 1 for client and 2 for admin\n"))
    if chr1 == 1:
        print("Enter 3 for login and 4 for register\n")
        ch2=int(input())

    elif chr1 == 2:
        adm = int(input("Press 3 for login and 4 to register !"))
    else:
        print("Enter valid options !")
except Exception as ex:
    print("Enter valid options only !")

##ADMIN REGISTRATION *****
if adm == 4:
    print("***** Welcome to register page *****")
    name = input('Enter First Name:')
    last_nm = input('Enter Last Name :')
    email_id = input('Enter Email-Id:')
    pass_wrd = input('Enter password:')
    sql = "INSERT INTO admin  VALUES ('" + name + "','" + last_nm + "','" + email_id + "','" + pass_wrd + "')"
    cursor.execute(sql)
    connect.commit()
    print("Admin Registered Successfully !")

# ******************    UPDATE BOOK PRICE BY ADMIN
def update_price():
    print("********** Welcome to price update page **********")
    book_nm = input("Enter the book name to update the price")
    price_bk = input("Enter the updated price !")
    query_update = "SELECT book FROM avail where book = '" + book_nm + "';"
    cursor.execute(query_update)
    record2 = cursor.fetchall()
    var = record2[0]
    print(var)
    if (book_nm in var):
        sql = "UPDATE avail SET price = '"+price_bk+"'where book = '"+book_nm+"';"
        cursor.execute(sql)
        connect.commit()
        print("\n Price Updated Successfully !")

#********            ADD NEW BOOK BY ADMIN
def add_book():
    book_nm1 = input("Enter the name of book to add")
    price_1 = input("Enter the price for the book !")
    # sql_ad = "INSERT INTO avail  VALUES ('" + book_nm1 + "','" + price_1 + "')"
    # cursor.execute(sql_ad)
    try:
        sql = "INSERT INTO avail (book, price) VALUES (%s, %s)"
        val = (book_nm1, price_1)
        cursor.execute(sql, val)
        connect.commit()
        print("New Book Added Successfully !")
    except Exception as ex:
        print("Cannot be added !")

#ADMIN LOGIN*****
if adm == 3:
    print("\n********* Welcome to admin panel *********")
    email_id = input('Enter Email-Id:')
    pass_wrd = input('Enter password:')

    try:
        query = "SELECT email AND password FROM admin where email = '"+email_id + "' and password = '"+pass_wrd+"';"
        cursor.execute(query)
        record = cursor.fetchall()
        if len(record) >= 1:
            print("Logged In Successfully  !\n")
            re = int(input("Press 1 to update book price and 2 for adding new books !"))
            if re == 1:
                update_price()
            elif re == 2:
                add_book()
        else:
            print("Enter valid credentials !")
    except Exception as ex:
        print("Enter valid Credentials !")

# **** CURRENTLY AVAILABLE BOOKS
def avl_book():
    avlb = "SELECT * from avail"
    cursor.execute(avlb)
    record1 = cursor.fetchall()

    for record in record1:
        print(str(record)[1:-1])
    pr = int(input("\nPress 1 to purchase book  and 2 to exit!"))
    try:
        if pr == 1:
            pur_book()
        elif pr == 2:
            exit()
        else:
            print("Enter valid choice ! \n")
            avl_book()
    except Exception as ex:
        print("Sorry this book is not available !")

#****** PURCHASE OPTION FOR CLIENT
def pur_book():
        clname = input("Enter your full name")
        email = input("Enter your email-id ")
        contact_no = input("Enter your contact no !")
        bkname = input("Enter the name of book to purchase !")
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        try:
            query4 = "SELECT * FROM avail where book = '" + bkname + "';"
            cursor.execute(query4)
            record2 = cursor.fetchall()
            var = record2[0]
            if bkname in var:
                sql = "INSERT INTO order_booked  VALUES ('" + clname + "','" + email + "','" + bkname + "','" + dt_string +"','"+contact_no+"')"
                cursor.execute(sql)
                connect.commit()
                print("\nOrder Placed Successfully !")
        except Exception as ex:
            print("Sorry "+clname+" This Book is not available !")

#**** CANCEL ORDER
def cancel_order():
    em = input("Enter your email-id !")
    try:
        cancelqu = "SELECT * FROM order_booked where email = '" + em + "';"
        cursor.execute(cancelqu)
        record3 = cursor.fetchall()
        var = record3[0]
        l1 = len(var)
        print("******* Welcome to view page *******")
        print("Your Order Details Are !")
        print(*var[0:l1+1])
        choice = input("Are you sure to cancel press y or n")
        if em in var:
            if choice == 'y':
                sql2 = "DELETE FROM order_booked WHERE email = '"+em+"';"
                cursor.execute(sql2)
                connect.commit()
                print("Order Cancelled Successfully !")
            else:
                print("Cancellation Failed !")
    except Exception as ex:
        print("Order not found !")


#REQUEST UNAVAILABLE BOOK
def request_bk():
    rq = input("Enter the book name !")
    try:
        sql = "INSERT INTO requestbook  VALUES ('" + rq+"')"
        cursor.execute(sql)
        connect.commit()
        print("\n This Book Will be available soon !")
    except Exception as ex:
        print("Cannot be make available !")


## Client REGISTER HERE *******
if ch2 == 4:
    lst = []
    print("***** Welcome to register page *****")
    name = input('Enter First Name:')
    lst.append(name)
    last_nm = input('Enter Last Name :')
    lst.append(last_nm)
    emailid = input('Enter Email-Id:')
    lst.append(emailid)
    passwrd = input('Enter password:')
    lst.append(passwrd)
    print(lst)
    sql = "INSERT INTO test  VALUES ('" + lst[0] + "','" + lst[1] + "','" + lst[2] + "','" + lst[3] + "')"
    cursor.execute(sql)
    connect.commit()
    print("Client Registered Successfully !")

### CLIENT LOGIN HERE ******
if ch2 == 3:
    print("***** Welcome to login page *****")
    emailid = input('Enter Email-Id:')
    passwrd = input('Enter password:')

    query = "SELECT email AND password FROM test where email = '"+emailid + "' and password = '"+passwrd+"';"
    cursor.execute(query)
    record=cursor.fetchall()
    if len(record) >= 1:
        print("Logged In Successfully  !")

        print("Press 1 to view available books !")
        print("Press 2 to cancel your order !")
        print("Press 3 to request a book !")
        avl = int(input())
        if avl == 1:
            avl_book()
        elif avl == 2:
            cancel_order()
        elif avl == 3:
            request_bk()
    else:
        print("Enter Valid Credentials !")
