from enum import Enum

# Enum for User Roles
class Role(Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"
    DELIVERY_STAFF = "Delivery Staff"

# Enum for Order Status
class OrderStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"

# Enum for Payment Status
class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"

# Class Customer
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number

    def display_customerInfo(self):
        print(f"Customer ID: {self.__customer_id}, Name: {self.__first_name} {self.__last_name}, Email: {self.__email}, Phone: {self.__phone_number}")

# Class Admin
class Admin:
    def __init__(self, admin_id, username, role, access_level):
        self.__admin_id = admin_id
        self.__username = username
        self.__role = role
        self.__access_level = access_level

    def display_adminInfo(self):
        print(f"Admin ID: {self.__admin_id}, Username: {self.__username}, Role: {self.__role.value}, Access Level: {self.__access_level}")

# Class Delivery Staff
class DeliveryStaff:
    def __init__(self, staff_id, first_name, last_name, status, vehicle_type):
        self.__staff_id = staff_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__status = status
        self.__vehicle_type = vehicle_type

    def display_deliveryStatus(self):
        print(f"Delivery Staff ID: {self.__staff_id}, Name: {self.__first_name} {self.__last_name}, Status: {self.__status}, Vehicle: {self.__vehicle_type}")

# Class Order
class Order:
    def __init__(self, order_id, customer_id, items, status, creation_date):
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__items = items
        self.__status = status
        self.__creation_date = creation_date

    def display_orderDetails(self):
        print(f"Order ID: {self.__order_id}, Customer ID: {self.__customer_id}, Items: {self.__items}, Status: {self.__status.value}, Date: {self.__creation_date}")

# Class Payment
class Payment:
    def __init__(self, payment_id, order_id, amount, payment_status):
        self.__payment_id = payment_id
        self.__order_id = order_id
        self.__amount = amount
        self.__payment_status = payment_status

    def display_paymentInfo(self):
        print(f"Payment ID: {self.__payment_id}, Order ID: {self.__order_id}, Amount: {self.__amount}, Status: {self.__payment_status.value}")

# Creating objects
customer1 = Customer(101, "Alice", "Smith", "alice@example.com", "+123456789")
customer2 = Customer(102, "Bob", "Johnson", "bob@example.com", "+987654321")

order1 = Order(401, 101, ["Item1", "Item2"], OrderStatus.CONFIRMED, "2025-02-28")
order2 = Order(402, 102, ["Item3", "Item4"], OrderStatus.SHIPPED, "2025-02-28")

payment1 = Payment(501, 401, 500.00, PaymentStatus.PENDING)
payment2 = Payment(502, 402, 750.00, PaymentStatus.COMPLETED)

staff1 = DeliveryStaff(301, "John", "Doe", "Available", "Bike")
staff2 = DeliveryStaff(302, "Jane", "Smith", "On Delivery", "Van")

admin1 = Admin(201, "adminAlice", Role.ADMIN, 5)
admin2 = Admin(202, "adminBob", Role.ADMIN, 4)

# Display object information
customer1.display_customerInfo()
customer2.display_customerInfo()
order1.display_orderDetails()
order2.display_orderDetails()
payment1.display_paymentInfo()
payment2.display_paymentInfo()
staff1.display_deliveryStatus()
staff2.display_deliveryStatus()
admin1.display_adminInfo()
admin2.display_adminInfo()
