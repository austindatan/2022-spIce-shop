import mysql.connector
mydb = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="austinreverie",
    database="spice")
db = mydb.cursor()

try:
    sql = "CREATE TABLE ordered_info (cart_id INT NOT NULL, " \
                "username VARCHAR(50)NOT NULL," \
                "product_name VARCHAR(100) NOT NULL, "\
                "price FLOAT NOT NULL, "\
                "`change` FLOAT NOT NULL," \
                "PRIMARY KEY (cart_id)) AUTO_INCREMENT = 100"
    db.execute(sql)
    mydb.commit()
    print("done")

except Exception as e:
    print("Error", e)