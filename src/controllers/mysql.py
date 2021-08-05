import os
from operator import itemgetter

mycursor = None
handler_name = 'mysql'


def get_instance():
    if mycursor is not None:
        return mycursor
    try:
        import mysql.connector
        mydb = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user="root",
            password=os.getenv('MYSQL_ROOT_PASSWORD'),
            database=os.getenv('MYSQL_DB'),
        )

        mycursor = mydb.cursor()
        print("MySql instance created: {}".format(mydb))
        return mycursor
    except Exception as e:
        print("Error in Mysql instance creation, please check MySql connector is installed and mysql configuration is correct")
        print("Exception : {}".format(e.__str__()))


def handler(args):
    q, = args
    get_instance()
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