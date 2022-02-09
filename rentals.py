from mysql.connector import MySQLConnection


# hard coded right now, if I'll have the time to
# set it in the .env and get all the names later in the right way , will do it
def connect_to_db():
    mydb = MySQLConnection(
        host="duplidb.cqxzpcrm4rdd.eu-west-1.rds.amazonaws.com",
        user="admin",
        password="root1234",
        database="movieRentalDB"
    )
    return mydb


def get_current_rentals():
    mydb = connect_to_db()
    my_cursor = mydb.cursor()
    my_cursor.callproc("current_rentals")
    ans = [result.fetchall() for result in my_cursor.stored_results()]
    my_cursor.close()
    return ans[0]
