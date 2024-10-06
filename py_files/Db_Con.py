import pymysql


con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11"
                    )

cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS AirwaysMS")
print("DB_Created")
cur.execute("USE AirwaysMS")
"""
cur.execute"(""CREATE TABLE IF NOT EXISTS Users(
                    u_id int(100), 
                    f_name varchar(100), 
                    l_name varchar(100),
                    u_name varchar(100),
                    gmail varchar(100),
                    password varchar(100),
                    ph_num int(15),
                    gender varchar(100),
                    dob varchar(100),
                    age int(4),
                    PRIMARY KEY (`u_id`)
            )"")"

print("Table Created")

cur.execut"e(""CREATE TABLE IF NOT EXISTS Flights(
                    f_id int(100), 
                    flight_name varchar(100), 
                    flight_num varchar(100), 
                    origin varchar(100),
                    destination varchar (100),
                    distance int(100),
                    price varchar (100),
                    date varchar(100),
                    PRIMARY KEY (`f_id`)
            )")

print("Table Created")"""


con.close()