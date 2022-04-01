import mysql.connector

from model.Factura import Factura
from services.Products_services import Products_services
class Facturas_services:
    def __init__(self) -> None:
        pass


    def get_facturas():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = "select * from factura;"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            facturas = []
            for row in records:
                products = {
                    "fertilizantes": Products_services.get_products_fertilizantes_by_factura_id(id=row[0]),
                    "control_de_plagas": Products_services.get_products_control_de_plagas_by_factura_id(id=row[0]),
                    "medicina_animal": Products_services.get_products_medicina_animal_by_factura_id(id=row[0]),
                }
                facturas.append(Factura(id=row[0], list_products=products))
                print("Id = ", row[0], )
                print("description = ", row[1], "\n")
            return facturas
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")