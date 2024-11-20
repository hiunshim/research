import json

from .models import Order, Product


def load_orders(file_path="database/CustomOrders.json"):
    with open(file_path, "r") as file:
        orders = json.load(file)
    return json.dumps(orders, indent=2)


def read_orders(file_path="database/CustomOrders.json") -> list[Order]:
    with open(file_path, "r") as file:
        orders = json.load(file)
    return [
        Order(
            customer_name=order["CustomerName"],
            email=order["Email"],
            order_number=order["OrderNumber"],
            products_ordered=order["ProductsOrdered"],
            status=order["Status"],
            tracking_number=order["TrackingNumber"],
        )
        for order in orders
    ]


def find_order(email: str, order_number: str):
    orders = read_orders()
    for order in orders:
        if equal_strings(order.email, email) or equal_strings(
            order.order_number, order_number
        ):
            return order


def load_products(file_path="database/ProductCatalog.json"):
    with open(file_path, "r") as file:
        products = json.load(file)
    return json.dumps(products, indent=2)


def read_products(file_path="database/ProductCatalog.json") -> list[Product]:
    with open(file_path, "r") as file:
        products = json.load(file)
    return [
        Product(
            product_name=product["ProductName"],
            sku=product["SKU"],
            inventory=product["Inventory"],
            description=product["Description"],
            tags=product["Tags"],
        )
        for product in products
    ]


def product_inventory():
    products = read_products()
    return [
        f"product: {product.product_name}, stock: {product.inventory}"
        for product in products
    ]


def product_descriptions():
    products = read_products()
    return ", ".join(
        [
            f"\nProduct: {product.product_name}, Description: {product.description}"
            for product in products
        ]
    )


# def find_product(product_name: str, order_number: str):
#     products = read_products()
#     for product in products:
#         if (
#             equal_strings(product.product_name, product_name)
#             or equal_strings(product.sku, sku)
#             or equal_strings(product.inventory, inventory)
#         ):
# return product

# def _search_products(
#     product_name=None, sku=None, inventory=None, description=None, tags=None
# ) -> list[Product]:
#     matches = []
#     for product in read_products():
#         match_count = 0
#         if (
#             product_name
#             and product_name.lower() == product.product_name.lower()
#         ):
#             match_count += 1
#         if sku and sku.lower() == product.sku.lower():
#             match_count += 1
#         if inventory and inventory == product.inventory:
#             match_count += 1
#         for product_tag in product.tags:
#             for tag in tags:
#                 if product_tag == tag:
#                     match_count += 1
#         if match_count > 0:
#             matches.append((match_count, product))
#     matches.sort(key=lambda x: -x["match_count"])
#     return [match[1] for match in matches]
#


def equal_strings(string1, string2):
    return (string1 or "").strip().lower() == (string2 or "").strip().lower()
