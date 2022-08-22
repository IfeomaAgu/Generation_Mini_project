from pickle import TRUE
import pymysql
import os
import pandas as pd
from sqlalchemy.engine import URL
from dotenv import load_dotenv

from Generation_Mini_project.All.courier_menu_details import a_space, multiple_space, view_courier
from Generation_Mini_project.All.product_menu_details import view_product
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# establish a database connection
def connect_to_database(): #call it whe you need it
    return pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database
)


connection_url = 'mysql+pymysql://root:password@localhost:3306/cafe_app'
from sqlalchemy import create_engine
engine = create_engine(connection_url)

def add_to_db(command):
    """ gets stuff from a db """
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"{command}") 
    connection.commit()
    cursor.close()
    connection.close()


def get_from_db(command):
    """ gets stuff from a db, returns the result """
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"{command}") 
    myresult = cursor.fetchall()
    connection.commit()
    return(myresult)

def print_title_stars(row): 
    stars = "**********************************************************************"
    print(stars)
    print(row)
    print(stars)

def view_orders():
        print_title_stars("Order list")
        order_list= 'SELECT Order_ID, name, address, phone, Courier_ID, Order_status, ordered_items FROM orders'
        order_list = pd.read_sql(order_list, engine)
        print(order_list.head())

def order_per__selected_courierID():      
        selected_courierID = int(input("Enter courier ID: "))
        list_orders_for_selected_courierID = f'SELECT Order_ID, name, address, phone, Courier_ID, Order_status, ordered_items FROM orders WHERE Courier_ID = {selected_courierID};'
        order_list = pd.read_sql(list_orders_for_selected_courierID, engine)
        print(order_list.head())
  
def order_by_order_status():
        list_order_by_order_status = 'SELECT Order_ID, Customer_name, Customer_address, Customer_phone, Chosen_Courier_ID, Order_status, ordered_items FROM orders ORDER BY Order_status;'
        order_list = pd.read_sql(list_order_by_order_status, engine)
        print(order_list.head())
        

order_status = ["Preparing", "On the way", "Delivered"]

def create_new_order(): 
        print_title_stars("Create a new order")
        customer_name = input("Full name: ")
        customer_address = input("Address: ")
        customer_phone = int(input("Phone number: "))
        view_product()
        a_space()
        product_index_value = list(input("Enter product IDs: ").split(',')) #list product for selection
        items = list(product_index_value)
        items = ",".join(items) #using join() to Join all items in a list into a string, using a comma character as separator
        view_courier()
        a_space()
        selected_courier = int(input("Enter courier ID: "))
        customer_order_status = "preparing"
        insert_order_statement = f"INSERT INTO orders(name, address, phone, Courier_ID, Order_status, ordered_items) VALUES {customer_name, customer_address, customer_phone, selected_courier, customer_order_status, items};"
        add_to_db(insert_order_statement)


def update_customer_order_details():
        print_title_stars("Update Order Property")
        a_space()
        view_orders()
        try:
            a_space()
            existing_order_ID = int(input("Enter order ID:"))
            multiple_space()
            print_title_stars("Update options")
            print("1. Update customer name", "2. Update Customer address", "3. Update Customer phone", "4. Update Courier ID", "5. Update Order status", "6. Update Ordered items", sep= "\n")
            a_space()
            update_option = int(input("Select update option: "))
            a_space()
            if update_option ==1:
                update_customer_name = input("Full name: ")
                customer_name = f"UPDATE orders SET name = '{update_customer_name}' WHERE  Order_ID = {existing_order_ID};"
                customer_name = add_to_db(customer_name)
            elif update_option ==2:
                update_customer_address = input("Address: ")
                customer_address = f"UPDATE orders SET address = '{update_customer_address}' WHERE  Order_ID = {existing_order_ID};"
                customer_address = add_to_db(customer_address)
            elif update_option ==3:
                update_customer_phone = int(input("Phone number: "))
                customer_phone = f"UPDATE orders SET phone = {update_customer_phone} WHERE  Order_ID = {existing_order_ID};"
                customer_phone = add_to_db(customer_phone)
            elif update_option ==4:
                product_list_with_ID =('SELECT Product_ID, Product_name, Product_price FROM products')
                product_list_with_ID = get_from_db(product_list_with_ID )
                print("Product Menu Options")
                for product in product_list_with_ID:
                    print (product)
                update_order_items = input("Enter product ID:")     
                customer_order_items = f"UPDATE orders SET phone = {update_order_items} WHERE  Order_ID = {existing_order_ID};"
                customer_order_items= add_to_db(customer_order_items)
            elif update_option ==5:
                for (i,item) in enumerate(order_status):
                        print(i,item)
                order_status_index_value = int(input("Enter order status:"))
                selected_order_status = order_status[order_status_index_value]
                order_status_update = (f"UPDATE orders SET Order_status = '{selected_order_status}' WHERE Order_ID = {existing_order_ID};")
                add_to_db(order_status_update)
                #order by courier or status
            elif update_option ==6:
                couriers_list = 'SELECT Courier_ID, Courier_name, Courier_phone FROM couriers'
                couriers_list = get_from_db(couriers_list)
                for courier in couriers_list:
                    print (courier)
                update_courier = int(input("Enter courier ID: ")) 
                update_courier = (f"UPDATE orders SET Chosen_Courier_ID = {update_courier} WHERE Order_ID = {existing_order_ID};")
                add_to_db(update_courier)
        except Exception as e:
            print(e)
            print("No update")
        
 
def delete_customer_order():
    print_title_stars("Delete order from order list")
    view_orders()
    a_space()
    delete_order_ID = int(input("Enter order number: "))
    delete_order= f"DELETE FROM orders WHERE Order_ID = {delete_order_ID};"
    add_to_db(delete_order)
       




