import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='228928125',
    database='tester'
)


mycursor = mydb.cursor()
mycursor.execute("Create table students(id int, first_name varchar(255), last_name varchar(255), email varchar(255))")

def addinfo():
    mycursor = mydb.cursor()
    sql = ("insert into students( id, first_name, last_name, email) values(%s, %s, %s, %s)")
    val = (1, "Alexey", "Popov", "myemail")
    mycursor.execute(sql, val)
    mydb.commit()

    mycursor.execute("select * from students")
    result = mycursor.fetchall()
    print(result)

    mycursor.execute("UPDATE `students` set first_name = 'Mars' WHERE first_name='Alexey'")
    result = mycursor.fetchall()
    mydb.commit()

print(addinfo())