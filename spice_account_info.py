import mysql.connector
mydb = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="austinreverie",
    database="spice")
db = mydb.cursor()

try:
    sql = "CREATE TABLE account_info (user_id INT AUTO_INCREMENT, " \
                "email VARCHAR(50)NOT NULL," \
                "password VARCHAR(100) NOT NULL, "\
                "PRIMARY KEY (cart_id)) AUTO_INCREMENT = 100"
    db.execute(sql)
    mydb.commit()
    print("done")

except Exception as e:
    print("Error", e)