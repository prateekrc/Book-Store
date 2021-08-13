from coon import connect, cursor
# import pyinputplus as pyip
import re
from datetime import datetime
now = datetime.now()

try:
    choice = int(input("Press 1 for buyer and 2 for admin (Only Numeric): \n"))

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    def check():
        email = input("Enter your email-id\n")
        if (re.match(regex, email)):
            return email
        else:
            print("Invalid Email")
            check()

    def isValid(s):
        pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        return pattern.match(s)

        ##CLIENT REGISTER HERE
    def fun():
        print("***** Welcome to client register panel *****")
        f_name = input("Enter your first name ")
        l_name = input('Enter your last name ')
        # email_id = input("Enter email ")
        email_id = check()
        pass1 = input("Enter password ")

        dict1 = {
        "firstname": f_name,
        "lastname": l_name,
        "email": email_id,
        "password": pass1
        }
        print(dict1)
        # sql = "INSERT INTO test  VALUES ('" + "firstname" + "','" + "lastname" + "','" + "email" + "','"
        # + "password" + "')"
        sql = "INSERT INTO test (firstname, lastname, email, password) values(%s, %s, %s, %s)"
        val = (dict1.get("firstname"), dict1.get("lastname"), dict1.get("email"), dict1.get("password"))
        cursor.execute(sql, val)
        connect.commit()
        n1 = int(input("Press 1 to register another user and 2 to exit !"))
        if n1 == 1:
            fun()
        elif n1 == 2:
            exit()
        else:
            print("Enter valid choice only !")
            exit()


    ##ADMIN REGISTRATION *****
    def adm_in():
        print("***** Welcome to register page *****")
        name = input('Enter First Name:\n')
        last_nm = input('Enter Last Name \n:')
        # email_id = input('Enter Email-Id:')
        email_id = check()
        pass_wrd = input('Enter password:\n')

        adm_dict = {
        "firstname":name,
        "lastname":last_nm,
        "email":email_id,
        "password":pass_wrd
        }

        print(adm_dict)
        # sql = "INSERT INTO admin  VALUES ('" + name + "','" + last_nm + "','" + email_id + "','" + pass_wrd + "')"
        # cursor.execute(sql)
        sql = "INSERT INTO admin (firstname, lastname, email, password) values(%s, %s, %s, %s)"
        val = (adm_dict.get("firstname"), adm_dict.get("lastname"), adm_dict.get("email"), adm_dict.get("password"))
        cursor.execute(sql, val)
        connect.commit()
        print("Admin Registered Successfully !")


    #****** PURCHASE OPTION FOR CLIENT
    def pur_book():
            clname = input("Enter your full name: ")
            # email = input("Enter your email-id: ")
            email= check()
            contact_no = input("Enter your contact no: !")

            if (isValid(contact_no)):
                bkname = input("Enter the name of book to purchase ! ")
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                pur_dict = {
                "name": clname,
                "email": email,
                "book_name": bkname,
                "ordered_on": dt_string,
                "mobile": contact_no
                }
                print(pur_dict)

                try:
                    query4 = "SELECT * FROM avail where book = '" + bkname + "';"
                    cursor.execute(query4)
                    record2 = cursor.fetchall()
                    var = record2[0]
                    if bkname in var:
                        sql = "INSERT INTO order_booked  VALUES ('" + pur_dict.get("name") + "','" + pur_dict.get("email") + "','" + pur_dict.get("book_name") + "','" + pur_dict.get("ordered_on") +"','"+pur_dict.get("mobile")+"')"
                        cursor.execute(sql)
                        connect.commit()
                        print("\nOrder Placed Successfully !")
                except Exception as ex:
                    print("Sorry "+clname+" This Book is not available !")
            else:
                print("Enter valid mobile no !")
                pur_book()


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


    # ******************    UPDATE BOOK PRICE BY ADMIN
    def update_price():
        print("********** Welcome to price update page **********")
        book_nm = input("Enter the book name to update the price")
        price_bk = input("Enter the updated price !")

        upd_dic = {
        "book":book_nm,
        "price":price_bk
        }
        print(upd_dic)

        query_update = "SELECT book FROM avail where book = '" + upd_dic.get("book") + "';"
        cursor.execute(query_update)
        record2 = cursor.fetchall()
        var = record2[0]
        print(var)
        if (book_nm in var):
            sql = "UPDATE avail SET price = '"+upd_dic.get("price")+"'where book = '"+upd_dic.get("book")+"';"
            cursor.execute(sql)
            connect.commit()
            print("\n Price Updated Successfully !")

    #********            ADD NEW BOOK BY ADMIN
    def add_book():
        book_nm1 = input("Enter the name of book to add ")
        price_1 = input("Enter the price for the book ! ")
        # s_no = input('Enter an id to arrange !: ')
        # sql_ad = "INSERT INTO avail  VALUES ('" + book_nm1 + "','" + price_1 + "')"
        # cursor.execute(sql_ad)
        add_dict = {
            # "sno": s_no,
            "book": book_nm1,
            "price": price_1
        }
        print(add_dict)
        try:
            sql = "INSERT INTO avail ( book, price) VALUES ( %s, %s)"
            val =  (add_dict.get("book"), add_dict.get("price"))  #(add_dict.get("sno"),
            cursor.execute(sql, val)
            connect.commit()
            print("New Book Added Successfully !")
        except Exception as ex:
            print("Cannot be added ! Try Again")
            add_book()


    #ADMIN LOGIN*****
    def adm_log():
        print("\n************** Welcome to admin panel **************")
        # email_id = input('Enter Email-Id:')
        email_id = check()
        pass_wrd = input('Enter password:')

        adm_log1 = {
        "email":email_id,
        "password":pass_wrd
        }

        print(adm_log1)

        try:
            query = "SELECT email AND password FROM admin where email = '"+adm_log1.get("email") + "' and password = '"+adm_log1.get("password")+"';"
            cursor.execute(query)
            record = cursor.fetchall()
            if len(record) >= 1:
                print("Logged In Successfully  !\n")
                print("Press 1 to update book price and 2 for adding new books !")
                re = int(input())
                if re == 1:
                    update_price()
                elif re == 2:
                    add_book()
            else:
                print("Enter valid credentials !")
        except Exception as ex:
            print("Enter valid Credentials !")

        ##ADMIN REGISTRATION *****
        def adm_in():
            print("***** Welcome to register page *****")
            name = input('Enter First Name:\n')
            last_nm = input('Enter Last Name \n:')
            # email_id = input('Enter Email-Id:')
            email_id = check()
            pass_wrd = input('Enter password:\n')

            adm_dict = {
                "firstname": name,
                "lastname": last_nm,
                "email": email_id,
                "password": pass_wrd
            }

            print(adm_dict)
            # sql = "INSERT INTO admin  VALUES ('" + name + "','" + last_nm + "','" + email_id + "','" + pass_wrd + "')"
            # cursor.execute(sql)
            sql = "INSERT INTO admin (firstname, lastname, email, password) values(%s, %s, %s, %s)"
            val = (adm_dict.get("firstname"), adm_dict.get("lastname"), adm_dict.get("email"), adm_dict.get("password"))
            cursor.execute(sql, val)
            connect.commit()
            print("Admin Registered Successfully !")


    def user_detail():
        em = input("Enter your email-id ! ")
        can_dict = {"email": em}
        print(can_dict)
        try:
            cancelqu = "SELECT * FROM order_booked where email = '" + can_dict.get("email") + "';"
            cursor.execute(cancelqu)
            record3 = cursor.fetchall()
            var = record3[0]
            l1 = len(var)
            print("******* Welcome to view page *******")
            print("Your Order Details Are !")
            print(*var[0:l1 + 1])
        except:
            print("Something went wrong !")

    #**** CANCEL ORDER
    def cancel_order():
        em = input("Enter your email-id ! ")
        can_dict = {"email": em}
        print(can_dict)
        try:
            cancelqu = "SELECT * FROM order_booked where email = '" + can_dict.get("email") + "';"
            cursor.execute(cancelqu)
            record3 = cursor.fetchall()
            var = record3[0]
            l1 = len(var)
            print("*************** Welcome to view page **************")
            print("Your Order Details Are !")
            print(*var[0:l1+1])
            choice = input("Are you sure to cancel press y or n ")
            if em in var:
                if choice == 'y' or 'Y':
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
        re_dict = {"book": rq}
        try:
            sql = "INSERT INTO requestbook  VALUES ('" + re_dict.get("book")+"')"
            cursor.execute(sql)
            connect.commit()
            print("\n This Book Will be available soon !")
        except Exception as ex:
            print("Cannot be make available !")

    ##CLIENT LOGIN HERE
    def cln_login():
        print("********** Welcome to login page **********")
        # emailid = input('Enter Email-Id:')
        emailid= check()
        # passwrd = input('Enter password:')
        passwrd = input('Enter password: ')

        log_dict = {
            "email" : emailid,
            "password" : passwrd
        }
        print(log_dict)
        query = "SELECT email AND password FROM test where email = '"+log_dict.get("email") + "' and password = '"+log_dict.get("password")+"';"
        cursor.execute(query)
        record=cursor.fetchall()
        if len(record) >= 1:
            print("Logged In Successfully  ! ")
            print("Press 1 to view available books ! ")
            print("Press 2 to view your order details ! ")
            print("Press 3 to request a book ! ")
            print("Press 4 to cancel your order ! \n")

            avl = int(input())
            if avl == 1:
                avl_book()
            elif avl == 4:
                cancel_order()
            elif avl == 3:
                request_bk()
            elif avl == 2:
                user_detail()
            else:
                print("Invalid selection !")
        else:
            print("Invalid Credentials ! Try again\n")
            cln_login()

    if choice == 1:
        cln = int(input("Press 2 for login and 3 for registration ! (Only Numeric): \n" ))
        if cln == 3:
            fun()
        elif cln == 2:
            cln_login()
        else :
            print("Enter valid options only ! ")

    if choice == 2:
        try:
            adm = int(input("Enter 2 for login and 3 for registration !(Only Numeric): \n"))
            if adm == 3:
                adm_in()
            elif adm == 2:
                adm_log()
        except:
            print("!!")
    else:
        print("! ")
except:
    print("Invalid Selection !")
