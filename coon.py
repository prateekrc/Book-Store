import mysql.connector

try:
    connect = mysql.connector.connect(host="localhost", username="root", password="root", database="test")
    cursor = connect.cursor()
    print("connection Established !")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))