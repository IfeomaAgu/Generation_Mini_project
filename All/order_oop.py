from Generation_Mini_project.All.product_menu_details import view_product

#trying to change order menu to OOP

class New_order:
    def __init__(self,name, address, phone, courier_ID, Order_status, ordered_items):
        self.name = name
        self.address = address
        self.phone = phone
        self.courier_ID = courier_ID
        self. Order_status= Order_status
        self.ordered_items = ordered_items

    
    def enter_ordered_items(self):
        while True:
               productname= int(input("Enter ordered items ID: "))
               quantity=int(input("Enter the quantity required: "))
               rate= f'SELECT price from products where ID = customer_items_ordered'
               totalamount= (quantity*rate)
        

        

customer_fullname = input("Enter full name: ")
customer_address = input("Enter address: ")
customer_phone = int(input("Enter phone number: "))
customer_courier_ID = int(input("Enter courier ID: "))
customer_Order_status = input("Enter Order status: ")
customer_ordered_items = input("Enter ordered items ID: ")

# customer_order = New_order(customer_fullname, customer_address, customer_phone, customer_courier_ID, customer_Order_status, customer_ordered_items)

def get_ordered_items(self):
    view_product
    customer_items_ordered = input("Enter ordered items ID: ")
    for item in customer_items_ordered:
        item_quantity= int(input("Enter quantity: "))
        cost_of_item = item_quantity * (f'SELECT price from products where ID = customer_items_ordered')
        return {"Product name":item, "quantity":item_quantity, "item_cost": cost_of_item}


class get_customer_order_info(New_order):
