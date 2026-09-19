# Product Store
"""
- Design and create an online store for products (name, price)
- Track total order being created
- Create a static method to calculate discount on each product based on a percentage parameter.
"""


class Product:
    count = 0  # Class attribute to track total orders

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1  # Increment the count for each new product instance

    @classmethod
    def get_total_products(cls):
        return cls.count

    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price - (price * discount_percentage / 100)


p1 = Product("Laptop", 1000)
p2 = Product("Smartphone", 500)

# Calculate discount for each product
discounted_price1 = Product.calculate_discount(p1.price, 10)  # 10% discount
discounted_price2 = Product.calculate_discount(p2.price, 20)  # 20% discount

print(f"Discounted price of {p1.name}: {discounted_price1:.2f}")
print(f"Discounted price of {p2.name}: {discounted_price2:.2f}")
print(f"Total products created: {Product.get_total_products()}")
