#--------------------------------------------PRODUCT-------------------------------------------------------------

from unicodedata import name
import csv 

product_name = ["club sandwhich", "cheese and ham toasty", "Beef burger", "Chicken burger", " Green tea", "Peppermint tea" "Americano", "Cappucino", "Latte","Apple juice", "Orange juice", "Coke Zero", "Coke", "Fanta", "Mango smoothie", "Soup of the day", "Donunts", "Muffin", "Scone", "Chocolate brownie", "Cheesecake", "Ben and Jerry's half baked", "Ben and Jerry's chocolate chip cookie dough"]
product_price = [8.99, 6.99, 10.99, 9.99, 2.50, 2.50, 3.0, 4.50, 4.50, 2.00, 2.00, 1.50, 1.50, 1.50, 3.50, 5.00, 4.00, 2.50, 2.50, 3.50, 4.20, 5.00, 5.00 ]


all_products = []


i=0
while i<22: #can use len(product_name)
    product_dictionary = {}
    product_dictionary["name"]=product_name[i]
    product_dictionary["price"]=product_price[i]
    #print(product_dictionary)
    i+=1
    all_products.append(product_dictionary)



def save_product_info_to_csv(all_products):
    with open('product_info.csv', mode='w') as file:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in all_products:
            writer.writerow(product)

save_product_info_to_csv(all_products)

#-----------------------------------------------COURIER-------------------------------------------------------------------------------------------

courier_name = ["John", "Claire", "Stephen", "Adam", "Beatrice", "Darren", "Emma", "Faith", "Garreth", "Harrison", "Chris"]
courier_phone = ["0789887889", "0789911001", "0722467900", "0779654321", "0711897856", "0745903466", "0752397705", "0734660293", "0767015588", "0701122644", "0703556640"]

all_courier = []
i=0
while i<11:
    courier_dictionary = {}
    courier_dictionary["name"]=courier_name[i]
    courier_dictionary["phone"]=courier_phone[i]
    #print(courier_dictionary)
    i+=1
    all_courier.append(courier_dictionary)


def save_courier_info_to_csv(all_courier):
    with open('courier_info.csv', mode='w') as file:
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for courier in all_courier:
            writer.writerow(courier)
save_courier_info_to_csv(all_courier)

#-------------------------------------------------ORDER-------------------------------------------------------------------------------------------------

def save_order_info_to_csv(order_list):
    with open('order_info.csv', mode='w') as file:
        fieldnames = ["customer_name", "customer_address", "customer_phone", "customer_comment", "courier", "order_status", "items"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for order in order_list:
            writer.writerow(order)

save_order_info_to_csv()















