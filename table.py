
import mysql.connector.pooling
import os
from dotenv import load_dotenv
load_dotenv()


dbconfig = {
    'host': os.getenv("SERVER_HOST"),
    'user': os.getenv("SERVER_USER"),
    'password': os.getenv("SERVER_PASSWORD"),
    'database': os.getenv("SERVER_DATABSE"),
    'charset': 'utf8',
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="pool",
    pool_size=5,
    pool_reset_session=True,
    **dbconfig
)
connection = connection_pool.get_connection()


mycursor = connection.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS posts(
id BIGINT AUTO_INCREMENT, message VARCHAR(255) NOT NULL, 
image_url VARCHAR(255) NOT NULL,
PRIMARY KEY (id))charset=utf8;
    """)  # InnoDB 儲存引擎 具備Commit, Rollback和當掉復原的事務處理能力，可保護使用者資料