import mysql.connector

class Products_services:

    def get_products_fertilizantes_by_factura_id(self, id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, ICA, frecuencia, fecha_de_aplicacion
            FROM relacion_factura_producto 
            INNER JOIN producto ON relacion_factura_producto.producto_id=producto.id 
            RIGHT JOIN producto_de_control ON producto.id = producto_de_control.producto_id 
            RIGHT JOIN fertilizantes ON producto_de_control.id = fertilizantes.producto_de_control_id 
            WHERE factura_id = %s"""
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, (id,))
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")

            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
    def get_products_control_de_plagas_by_factura_id(self, id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, ICA, frecuencia, periodo_de_carencia    
            FROM relacion_factura_producto 
            INNER JOIN producto ON relacion_factura_producto.producto_id=producto.id 
            RIGHT JOIN producto_de_control ON producto.id = producto_de_control.producto_id 
            RIGHT JOIN control_de_plagas ON producto_de_control.id = control_de_plagas.producto_de_control_id 
            WHERE factura_id = %s"""
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, (id,))
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")
                
            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")

                
    def get_products_medicina_animal_by_factura_id(self, id):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, animal, dosis
            FROM relacion_factura_producto 
            INNER JOIN producto ON relacion_factura_producto.producto_id=producto.id 
            RIGHT JOIN medicina_animal ON producto.id = medicina_animal.producto_id 
            WHERE factura_id = %s"""
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, ("""1""",))
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")
            
            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")


    def get_all_products_medicina_animal(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, animal, dosis
            FROM producto 
            RIGHT JOIN medicina_animal ON producto.id = medicina_animal.producto_id """
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")
            
            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
    def get_all_products_control_de_plagas(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, ICA, frecuencia, periodo_de_carencia    
            FROM producto
            RIGHT JOIN producto_de_control ON producto.id = producto_de_control.producto_id 
            RIGHT JOIN control_de_plagas ON producto_de_control.id = control_de_plagas.producto_de_control_id """
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, (id,))
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")
                
            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")


    def get_all_products_fertilizantes():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='billing',
                                                user='root',
                                                password='admin123')

            sql_select_Query = """SELECT producto.id, producto.nombre, producto.precio, ICA, frecuencia, fecha_de_aplicacion
            FROM producto 
            RIGHT JOIN producto_de_control ON producto.id = producto_de_control.producto_id 
            RIGHT JOIN fertilizantes ON producto_de_control.id = fertilizantes.producto_de_control_id """
            cursor = connection.cursor()
            cursor.execute(sql_select_Query, (id,))
            # get all records
            records = cursor.fetchall()
            print("Total number of rows in table: ", cursor.rowcount)

            print("\nPrinting each row")
            for row in records:
                
                print("Id = ", row[0], "\n")

            return records

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")