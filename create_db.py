import mysql.connector
import sys
import time

def debug_print(message):
    print(message)
    sys.stdout.flush()

debug_print("Script started...")

conn = None
cursor = None

try:
    # Use the working parameters: "localhost" with port 3306
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="@Wambura2002",
        connection_timeout=10,
        use_pure=True
    )
    debug_print("Connected to MySQL successfully!")
    
    cursor = conn.cursor()
    
    database_name = "Naomi"
    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    debug_print(f"Database '{database_name}' created successfully!")
    
    # List all databases to confirm creation
    cursor.execute("SHOW DATABASES;")
    databases = cursor.fetchall()
    debug_print("Current databases on the server:")
    for db in databases:
        debug_print(db[0])
    
except mysql.connector.Error as err:
    debug_print(f"MySQL Error: {err}")
except Exception as e:
    debug_print(f"General error: {e}")
    
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
    debug_print("Script finished!")
