def update_order_status(order, new_status):
    order["order_status"] = new_status
    return order

