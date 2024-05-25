
def order_schema(order) -> dict:
    return {
        "id": str(order["_id"]),
        "cod_order": order["cod_order"],
        "username": order["username"],
        "id_product": order["id_product"]}

def orders_schema(orders) -> list:
    return [order_schema(order) for order in orders]