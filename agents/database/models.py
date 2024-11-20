import json


class Order:
    def __init__(
        self,
        customer_name="",
        email="",
        order_number="",
        products_ordered=[],
        status="",
        tracking_number="",
    ):
        self.customer_name = customer_name
        self.email = email
        self.order_number = order_number
        self.products_ordered = (
            products_ordered if products_ordered is not None else []
        )
        self.status = status
        self.tracking_number = tracking_number
        self.tracking_link = (
            f"https://tools.usps.com/go/TrackConfirmAction?tLabels={self.tracking_number}"
            if self.tracking_number
            else ""
        )

    def __repr__(self):
        return f"""
            Name: {self.customer_name}
            Email: {self.email}
            Order Number: {self.order_number}
            Products Ordered: {self.products_ordered}
            Status: {self.status}
            Tracking Number: {self.tracking_number}
            Tracking Link: {self.tracking_link}
            """

    def to_json(self):
        return json.dumps(
            {
                "CustomerName": self.customer_name,
                "Email": self.email,
                "OrderNumber": self.order_number,
                "ProductsOrdered": self.products_ordered,
                "Status": self.status,
                "TrackingNumber": self.tracking_number,
                "TrackingLink": self.tracking_link,
            }
        )


class Product:
    def __init__(
        self, product_name="", sku="", inventory=0, description="", tags=[]
    ):
        self.product_name = product_name
        self.sku = sku
        self.inventory = inventory
        self.description = description
        self.tags = tags

    def __repr__(self):
        return f"""
            Product: {self.product_name}
            SKU: {self.sku}
            Inventory: {self.inventory}
            Description: {self.description}
            Tags: {self.tags}
            """

    def to_json(self):
        return json.dumps(
            {
                "ProductName": self.product_name,
                "SKU": self.sku,
                "Inventory": self.inventory,
                "Description": self.description,
                "Tags": self.tags,
            }
        )
