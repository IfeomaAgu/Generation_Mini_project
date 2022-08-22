
from Generation_Mini_project.All.courier_menu_details import add_new_courier, delete_courier, update_courier_details, view_courier
from Generation_Mini_project.All.order_menu_details import create_new_order, delete_customer_order, order_by_order_status, order_per__selected_courierID, update_customer_order_details, view_orders
from Generation_Mini_project.All.product_menu_details import create_new_product, delete_product_from_product_list, update_product_details, view_product


def print_title_stars(row): 
    stars = "**********************************************************************"
    print(stars)
    print(row)
    print(stars)

def one_space():
    print(sep = "\n")

def large_space():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")


def product_main_menu():
    product_menu = ["Return to main menu", "View products", "Create new product", "Update product details", "Delete product", "Export file"]
    for (i,item) in enumerate (product_menu, start = 0):
            print(i, item)
    one_space()  
    product_menu_options= int(input("Select option: "))
    large_space()
    if product_menu_options==1:
        view_product()
        large_space()
        print_title_stars("Product Main Menu")
        product_main_menu()
    elif product_menu_options==2:
        create_new_product()
        one_space()
        print_title_stars("Product Main Menu")
        product_main_menu()
    elif product_menu_options==3:
        update_product_details()
        one_space()
        print_title_stars("Product Main Menu")
        product_main_menu() 
    elif product_menu_options==4:
        delete_product_from_product_list()
        one_space()
        print_title_stars("Product Main Menu")
        product_main_menu() 
    else:
        product_menu_options==0
        main_menu()         
    
    

def couriers_main_menu():
    couriers_menu = ["Return to main menu", "View couriers", "Add new courier", "Update courier details", "Delete courier", "Export file"]
    for (i,item) in enumerate (couriers_menu, start = 0):
            print(i, item)     
    one_space()  
    couriers_menu_options= int(input("Select option: "))
    large_space()
    if couriers_menu_options==1:
        view_courier()
        large_space()
        print_title_stars("Couriers Main Menu")
        couriers_main_menu()
    elif couriers_menu_options==2:
        add_new_courier()
        large_space()
        print_title_stars("Couriers Main Menu")
        couriers_main_menu()
    elif couriers_menu_options==3:
        update_courier_details()
        large_space()
        print_title_stars("Couriers Main Menu")
        couriers_main_menu()
    elif couriers_menu_options==4:
        delete_courier()
        large_space()
        print_title_stars("Couriers Main Menu")
        couriers_main_menu()
    else:
        couriers_menu_options==0
        main_menu() 

def order_main_menu():
    order_menu = ["Return to main menu", "View orders", "Create new order", "Update order details", "Delete order", "Export file"]
    for (i,item) in enumerate (order_menu, start = 0):
            print(i, item)     
    print(sep = "\n")
    order_menu_options= int(input("Select option: "))
    if order_menu_options==1:
        print("1. View all order", "2. View order by courier", "3. View order by order status", sep="\n")
        one_space()
        view_option = int(input("Enter option: "))
        if view_option == 1:
            view_orders()
            large_space()
            print_title_stars("Order Main Menu")
            order_main_menu()
            large_space()
        elif view_option == 2:
            order_per__selected_courierID()
            large_space()
            print_title_stars("Order Main Menu")
            order_main_menu()
            large_space()
        elif view_option == 2:
            order_by_order_status()
            large_space()
            print_title_stars("Order Main Menu")
            order_main_menu()
            large_space()
        
    elif order_menu_options==2:
        create_new_order()
        large_space()
        print_title_stars("Order Main Menu")
        order_main_menu()
        large_space()
    elif order_menu_options==3:
        update_customer_order_details()
        large_space()
        print_title_stars("Order Main Menu")
        order_main_menu()
        large_space()
    elif order_menu_options==4:
        delete_customer_order()
        large_space()
        print_title_stars("Order Main Menu")
        order_main_menu()
        large_space()
    else:
        order_menu_options==0
        main_menu()




def main_menu():
    print_title_stars("Main Menu")
    main_menu_options=["Exit Main Menu", "Product Menu", "Courier Menu", "Order Menu"]
    for (i,item) in enumerate (main_menu_options, start = 0):
        print(i, item) 
    one_space()
    select_main_menu_options = int(input("Please enter menu option number: "))
    large_space()
    if select_main_menu_options==1:
        print_title_stars("Product Main Menu")
        product_main_menu()
    elif select_main_menu_options == 2:
        print_title_stars("Couriers Main Menu")
        couriers_main_menu()
    elif select_main_menu_options == 3:
        print_title_stars("Order Main Menu")
        order_main_menu()
    else:
         select_main_menu_options == 0 
         return exit()





