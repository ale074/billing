import mysql.connector

from model.Factura import Factura
def get_facturas():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='billing',
                                            user='root',
                                            password='admin123')

        sql_select_Query = "select * from factura"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        facturas = []
        for row in records:
            productos = {}
            facturas.append(Factura(id=row[0], list_products=productos))
            print("Id = ", row[0], )
            print("description = ", row[1], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")