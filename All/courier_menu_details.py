from pickle import TRUE
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def database_connection():
    return pymysql.connect(
    host,
    user,
    password,
    database
)

def print_title_stars(row): 
    stars = "**********************************************************************"
    print(stars)
    print(row)
    print(stars)


def a_space():
    print(sep = "\n")

def multiple_space():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

def view_courier():
    print_title_stars("Couriers list")
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT ID, Name, Phone FROM couriers')
    product_list = cursor.fetchall()
    for row in product_list:
        print(f'ID:{row[0]}, Name:{row[1]}, Phone:{row[2]}')



def add_new_courier():
    new_courier_suggestion = {}
    new_courier_name=input("Enter new courier's name: ")
    new_courier_phone = int(input("Enter new courier's phone number: "))
    new_courier_suggestion["name"] = new_courier_name
    new_courier_suggestion["phone"] = new_courier_phone
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO couriers(Name, Phone) VALUES ('{new_courier_name}', {new_courier_phone});")
    connection.commit()
    cursor.close()
    connection.close



def update_courier_details(): 
    print_title_stars("Update Courier's Details") 
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT ID, Name, Phone FROM couriers')
    couriers_list = cursor.fetchall()
    for row in couriers_list:
        print(f'ID:{row[0]}, Name:{row[1]}, Phone:{row[2]}')
    try:
        a_space()
        existing_courier_ID = int(input("Enter courier ID:"))
        multiple_space()
        print_title_stars("Update options")
        print("1. Update courier's name", "2. Update courier's phone number", sep= "\n")
        a_space()
        update_option = int(input("Select update option: "))
        a_space()
        if update_option ==1:
            existing_courier_new_name = input("Enter new name for courier: ")
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(f"UPDATE couriers SET name='{existing_courier_new_name}' WHERE ID = {existing_courier_ID};")
            connection.commit()
            cursor.close()
            connection.close
            print("Courier updated")
        else:
            update_option ==2
            existing_courier_new_phone = int(input("Enter courier's new phone number:"))
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(f"UPDATE couriers SET Phone={existing_courier_new_phone} WHERE ID = {existing_courier_ID };")
            connection.commit()
            cursor.close()
            connection.close
            print("Courier updated")
    except Exception as e:
            print(e)
            print("No update")



def delete_courier():
    print_title_stars("Delete product from product list")
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT ID, Name, Phone FROM couriers')
    courier_list_with_ID = cursor.fetchall()
    for row in courier_list_with_ID:
        print(f'ID:{row[0]}, Name:{row[1]}, Phone:{row[2]}')
    a_space()
    courier_number= int(input("Enter courier ID: "))
    cursor.execute(f"DELETE FROM couriers WHERE ID = {courier_number};")
    connection.commit()
    cursor.close()
    connection.close()
 
