from pickle import TRUE
import pymysql
import os
from dotenv import load_dotenv


load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

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

# Establish a database connection
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




def view_product():
    print_title_stars("Product list")
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT ID, Name, Price FROM products")
    product_list = cursor.fetchall()
    for row in product_list:
        print(f'ID:{row[0]}, Name:{row[1]}, Price:{row[2]}')


#data validation(give exmaple of number), re-enter when error occurs, 
def create_new_product():
    print_title_stars("Create a new product")
    new_product_name = input("Suggest new name for new product: ")
    new_product_price = float(input("Enter new product price: "))
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO products(Name, Price) VALUES ('{new_product_name}', {new_product_price});")
    connection.commit()
    cursor.close()
    connection.close



def update_product_details(): #name or price
    print_title_stars("Update Product Details") 
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT ID, Name, Price FROM products')
    product_list_with_ID = cursor.fetchall()
    for row in product_list_with_ID:
        print(f'ID:{row[0]}, Name:{row[1]}, Price:{row[2]}')
    try:
        a_space()
        existing_product_ID = int(input("Enter product number:"))
        multiple_space()
        print_title_stars("Update options")
        print("1. Update product name", "2. Update product price", sep= "\n")
        a_space()
        update_option = int(input("Select update option: "))
        a_space()
        if update_option == 1:
            product_name_suggestion = input("Suggest new name for selected product: ")     
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(f"UPDATE products SET name = '{product_name_suggestion}' WHERE ID = {existing_product_ID};")
            connection.commit()
            cursor.close()
            connection.close()
            print("Product updated")
        else: 
            update_option == 2
            product_price_suggestion = float(input("Please enter your price suggestion: "))
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(f"UPDATE products SET price = {product_price_suggestion} WHERE ID = {existing_product_ID};")
            connection.commit()
            cursor.close()
            connection.close()
            print("Product updated")
    except Exception as e:
                print(e)
                print("No update")

           

def delete_product_from_product_list():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT ID, name, price FROM products')
    product_list_with_ID = cursor.fetchall()
    for product in product_list_with_ID:
        print (product)
    product_number= int(input("Enter product number: "))
    cursor.execute(f"DELETE FROM products WHERE ID = {product_number};")
    connection.commit()
    cursor.close()
    connection.close()
    print("succesfully deleted")
    
