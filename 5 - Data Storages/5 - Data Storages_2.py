# 2.  Follow this tutorial:
# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# to install psycopg2 which is the Python module that we will be using to connect to postgreSQL from Python code. 

# *You may need to install pip: sudo apt install python3-pip

# As a solution, implement python script that executes SELECT version() in our database and print the result.
# The script also generates 100 rows of randomized measurement data into the measurements table. 
# You can freely choose what kind of measurement unit you want (temperature, humidity, whatever you want).
# After generating the data, the script queries the table for 10 highest values of the measurement field 
# and prints those on screen.

import psycopg2
import random

def randomize_ver_select():
    """ insert from data_list into the measurements table  """
    sql_query = """INSERT INTO measurements (measurement, measurement_unit) VALUES(%s, %s);"""
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="your_db_name",
            user="your_username",
            password="your_password"
        )
        db_cursor = conn.cursor()
        
        data_list = []
        for num in range(100):
            data_list.append([])
            #data_list[num].append(round(random.uniform(-35.0, 39.9), 1))
            data_list[num].append(random.randint(1, 99))
            data_list[num].append("℃")
        
        # execute all the INSERT statements
        db_cursor.executemany(sql_query, data_list)

        print("Database version for PostgreSQL: ")
        db_cursor.execute("""SELECT version();""")
        db_version = db_cursor.fetchone()
        print(db_version[0], "\n")

        print("10 highest values of the measurement field: \n")
        db_cursor.execute("""SELECT * FROM measurements ORDER BY measurement DESC LIMIT 10;""")
        result = db_cursor.fetchall()
        for row in result:
            print("measurement_id =", row[0])
            print("measurement =", row[1])
            print("measurement_unit =", row[2], "\n")

        # close communication with the PostgreSQL database server
        db_cursor.close()
        # commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("All database connections terminated.")

if __name__ == '__main__':
    randomize_ver_select()