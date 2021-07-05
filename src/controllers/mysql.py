from operator import itemgetter

try:
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="K2test"
    )

    mycursor = mydb.cursor()
    print("MySql instance created: {}".format(mydb))
except Exception as e:
    print("Error in Mysql instance creation, please check MySql connector is installed and mysql configuration is correct")
    print("Exception : {}".format(e.__str__()))

handler_name = 'mysql'

def handler(args):
    q, = args
    data = mysql_execute(q)
    return data

def mysql_execute(data):
    email, password = itemgetter('email', 'password')(data)
    print("Email : {}, password : {}".format(email, password))
    query = "SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'"
    print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    return myresult