
from mp_functions import update_order_status

def test_update_order_status():
    order_list = [
    {"customer_name": "Jack", 
    "customer_address": "14 west", 
    "customer_phone": "0918777", 
    "customer_comment": "no", 
    "courier": "0", 
    "order_status": "preparing"}, 
    {"customer_name": "Jenny", 
    "customer_address": "12 east", 
    "customer_phone": "0987666", 
    "customer_comment": "no tomato", 
    "courier": "2", 
    "order_status": "preparing"}]

    order_index_value = 0
    new_status = "on the way"
    expected = "on the way"
    selected_order = order_list[order_index_value]
    order_list[order_index_value] = update_order_status(selected_order, new_status)
    actual = order_list[order_index_value]["order_status"]
    assert expected == actual 



