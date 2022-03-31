from mysql.connector import Error
from mysql.connector import pooling

def get_connection():
    try:
        connection_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                    pool_size=5,
                                                    pool_reset_session=True,
                                                    host='localhost',
                                                    database='billing',
                                                    user='root',
                                                    password='admin123')

        print("Printing connection pool properties ")
        print("Connection Pool Name - ", connection_pool.pool_name)
        print("Connection Pool Size - ", connection_pool.pool_size)

        # Get connection object from a pool
        return connection_pool.get_connection()
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)