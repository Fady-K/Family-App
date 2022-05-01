import sqlite3
import pandas as pd
##############
# Functions related to data base


# created connection and cursor
conn = sqlite3.connect("Kins.db")
c = conn.cursor()


# create table
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS Family (
    id integer PRIMARY KEY,
    First_name text, 
    Last_name text, 
    Kinship text,
    Age integer,
    Address text,
    Mobile integer,
    Email text
    )""")


# add_kin takes a kin data from user and insert them as new kin to database
def add_kin(first_name=None, last_name=None, kinship=None, age=None, address=None, mobile=None, email=None):
    with conn:
        c.execute("INSERT INTO Family (First_name, Last_name, Kinship, Age, Address, Mobile, Email) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, kinship, age, address, mobile, email))


# get_all_kins returns all the kins in a formatted table using pandas module
def get_all_kins():
    pd.set_option('display.max_rows', 500)      # this configuration helps to display all existing columns
    pd.set_option('display.max_columns', 500)   # to display all existing rows
    pd.set_option('display.width', 1000)        # to display the table's original width
    with conn:
        get_all_columns = "SELECT * FROM Family"
        return pd.read_sql_query(get_all_columns, conn)


# get_kin_by_name takes a kin first_name and last_name, Then return the kin
def get_kin_by_name(first_name, last_name):
    with conn:
        kins = c.execute("SELECT * FROM Family WHERE First_name = ? AND Last_name = ?", (first_name, last_name))
        list_of_kins = kins.fetchall()
        for kin in list_of_kins:
            return kin


# get_oldest_kin sorts table in desc order and then returns the first kin (the oldest)
def get_oldest_kin():
    with conn:
        kin = c.execute("""
            SELECT * FROM Family
            ORDER BY Age DESC
            LIMIT 1
            """)
        return kin.fetchone()


# get_oldest_kin sorts table in asc order and then returns the first kin (the youngest)
def get_youngest_kin():
    with conn:
        kin = c.execute("""
            SELECT * FROM Family
            ORDER BY Age ASC
            LIMIT 1
            """)
        return kin.fetchone()


# delete_kin uses DELETE query to delete a kin (ROW) from the table
def delete_kin(first_name, last_name):
    c.execute("DELETE FROM Family WHERE First_name = ? AND Last_name = ?", (first_name, last_name))


# update_age uses UPDATE query to update a kin's age
def update_age(first_name, last_name, new_age):
    c.execute("UPDATE Family SET Age = ? WHERE First_name = ? AND Last_name = ?", (new_age, first_name, last_name))


# update_address uses UPDATE to update a kin's address
def update_address(first_name, last_name, new_address):
    c.execute("UPDATE Family SET Address = ? WHERE First_name = ? AND Last_name = ?", (new_address, first_name, last_name))


# update_mobile uses UPDATE query to update a kin's mobile number
def update_mobile(first_name, last_name, new_mobile):
    c.execute("UPDATE Family SET Mobile = ? WHERE First_name = ? AND Last_name = ?", (new_mobile, first_name, last_name))


# update_email uses UPDATE query to update a kin's email
def update_email(first_name, last_name, new_email):
    c.execute("UPDATE Family SET Email = ? WHERE First_name = ? AND Last_name = ?", (new_email, first_name, last_name))


# clear_table clears all kins in the table
def clear_table():
    c.execute("DELETE FROM Family")


# return columns names in a tuple
def columns_names():
    c.execute("SELECT * FROM Family WHERE 1=0")
    list_of_columns = [x[0] for x in c.description]
    return tuple(list_of_columns)

