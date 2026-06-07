from utils.db_connection import get_connection

try:
    conn = get_connection()

    if conn.is_connected():
        print("Database Connected Successfully!")

    conn.close()

except Exception as e:
    print("Error:", e)