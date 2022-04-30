from unittest import result
import mysql.connector.pooling
from mysql.connector import Error
from dotenv import load_dotenv
import os
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
def connection_db(sql,value):
    try:
        connection = connection_pool.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, value)
        
        
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)

    finally:
        result=mycursor.fetchall()
        connection.commit()
        if connection.in_transaction:
            connection.rollback()
        mycursor.close()
        connection.close()
        return result
def insert_upload_data(message=None,image_url=None):
    if message and image_url:
        sql="INSERT INTO posts (message,image_url) VALUES (%s,%s)"
        val=(message,image_url)
        result=connection_db(sql,val)
        if result:
            return True
        else:
            return None
def search_upload_data():
    sql="SELECT message,image_url from posts"
    val=()
    results=connection_db(sql,val)
    result_list=[]
    if results:
        for result in results:
            data={
                "message":result[0],
                "image_url":result[1]
            }
            result_list.append(data)
        return result_list
    else:
        return None
            
    
    
def allowed_file(filename):
    
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"png", "jpg", "jpeg"}
        
        
    