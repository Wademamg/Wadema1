# Ticket Class - Composition with Event (1-to-1)
class Ticket:
    def __init__(self, ticket_id, ticket_type, price, validity, features, event_details):
        try:
            self._ticket_id = ticket_id
            self._ticket_type = ticket_type
            self._price = price
            self._validity = validity
            self._features = features
 # Create new Event INSIDE Ticket -> True Composition
            self._event = Event(**event_details)        
        except Exception as e:
            print(f"Error initializing Ticket: {e}")

    def set_ticket_id(self, id): self._ticket_id = id
    def get_ticket_id(self): return self._ticket_id

    def set_ticket_type(self, t): self._ticket_type = t
    def get_ticket_type(self): return self._ticket_type

    def set_price(self, p): self._price = p
    def get_price(self): return self._price

    def set_validity(self, v): self._validity = v
    def get_validity(self): return self._validity

    def set_features(self, f): self._features = f
    def get_features(self): return self._features

    def set_event(self, event): self._event = event
    def get_event(self): return self._event

    def display(self):
        print(f"Ticket ID: {self._ticket_id}, Type: {self._ticket_type}, Price: {self._price}, Validity: {self._validity}, Features: {self._features}")
        self._event.display()


# Event Class - Referenced by Ticket (composition) and Admin (aggregation)
class Event:
    def __init__(self, event_id, name, date, venue, description):
        try:
            self._event_id = event_id
            self._name = name
            self._date = date
            self._venue = venue  # Can be a Venue object or string
            self._description = description
        except Exception as e:
            print(f"Error initializing Event: {e}")

    def set_event_id(self, e): self._event_id = e
    def get_event_id(self): return self._event_id

    def set_name(self, n): self._name = n
    def get_name(self): return self._name

    def set_date(self, d): self._date = d
    def get_date(self): return self._date

    def set_venue(self, v): self._venue = v
    def get_venue(self): return self._venue

    def set_description(self, desc): self._description = desc
    def get_description(self): return self._description

    def display(self):
        print(f"Event ID: {self._event_id}, Name: {self._name}, Date: {self._date}, Venue: {self._venue}, Description: {self._description}")

# SeasonMembership Class - Has list of races (races_included)
class SeasonMembership:
    def __init__(self, season_year, races_included=None, member_benefits=None, renewal_date=None):
        try:
            self._season_year = season_year
            self._races_included = races_included if races_included is not None else [] # LIST ASSOCIATION: list of race names or IDs
            self._member_benefits = member_benefits
            self._renewal_date = renewal_date
        except Exception as e:
            print(f"Error initializing SeasonMembership: {e}")

    def set_season_year(self, y): self._season_year = y
    def get_season_year(self): return self._season_year

    def set_races_included(self, r): self._races_included = r
    def get_races_included(self): return self._races_included

    def set_member_benefits(self, b): self._member_benefits = b
    def get_member_benefits(self): return self._member_benefits

    def set_renewal_date(self, d): self._renewal_date = d
    def get_renewal_date(self): return self._renewal_date

    def display(self):
        print(f"Season: {self._season_year}, Renewal: {self._renewal_date}, Benefits: {self._member_benefits}, Races: {self._races_included}")

# User Class - Base class for Admin and Customer
class User:
    def __init__(self, user_id, name, email, password, role):
        try:
            self._user_id = user_id
            self._name = name
            self._email = email
            self._password = password
            self._role = role
        except Exception as e:
            print(f"Error initializing User: {e}")

    def set_user_id(self, uid): self._user_id = uid
    def get_user_id(self): return self._user_id

    def set_name(self, n): self._name = n
    def get_name(self): return self._name

    def set_email(self, e): self._email = e
    def get_email(self): return self._email

    def set_password(self, pw): self._password = pw
    def get_password(self): return self._password

    def set_role(self, r): self._role = r
    def get_role(self): return self._role

    def authenticate(self, pw): return self._password == pw

    def display(self):
        print(f"User ID: {self._user_id}, Name: {self._name}, Role: {self._role}")


# Admin Class - Inherits from User and Aggregates Events (0..* Event)
class Admin(User):
    def __init__(self, user_id, name, email, password, role, admin_id, permissions=None, department=None, managed_events=None):
        super().__init__(user_id, name, email, password, role)
        try:
            self._admin_id = admin_id
            self._permissions = permissions if permissions is not None else []
            self._department = department
            self._managed_events = managed_events if managed_events is not None else []  # AGGREGATION: list of Event objects managed by Admin
        except Exception as e:
            print(f"Error initializing Admin: {e}")

    def set_admin_id(self, id): self._admin_id = id
    def get_admin_id(self): return self._admin_id

    def set_permissions(self, p): self._permissions = p
    def get_permissions(self): return self._permissions

    def set_department(self, d): self._department = d
    def get_department(self): return self._department

    def set_managed_events(self, ev): self._managed_events = ev
    def get_managed_events(self): return self._managed_events

    def view_sales_report(self): print("Viewing sales report...")

    def display(self):
        super().display()
        print(f"Admin ID: {self._admin_id}, Department: {self._department}")
        for event in self._managed_events:
            event.display()


# Customer Class - Inherits from User and is associated with PurchaseOrders
class Customer(User):
    def __init__(self, user_id, name, email, password, role, loyalty_points, phone_number, address, purchase_orders=None):
        super().__init__(user_id, name, email, password, role)
        try:
            self._loyalty_points = loyalty_points
            self._phone_number = phone_number
            self._address = address
            self._purchase_orders = purchase_orders if purchase_orders is not None else []
        except Exception as e:
            print(f"Error initializing Customer: {e}")

    def set_loyalty_points(self, p): self._loyalty_points = p
    def get_loyalty_points(self): return self._loyalty_points

    def set_phone_number(self, p): self._phone_number = p
    def get_phone_number(self): return self._phone_number

    def set_address(self, a): self._address = a
    def get_address(self): return self._address

    def set_purchase_orders(self, po): self._purchase_orders = po
    def get_purchase_orders(self): return self._purchase_orders

    def update_details(self): print("Customer details updated.")

    def display(self):
        super().display()
        print(f"Phone: {self._phone_number}, Address: {self._address}, Loyalty Points: {self._loyalty_points}")
        for order in self._purchase_orders:
            order.display()


# Payment Class - Associated with one PurchaseOrder
class Payment:
    def __init__(self, payment_id, method, amount, status, date):
        try:
            self._payment_id = payment_id
            self._method = method
            self._amount = amount
            self._status = status
            self._date = date
        except Exception as e:
            print(f"Error initializing Payment: {e}")

    def set_payment_id(self, id): self._payment_id = id
    def get_payment_id(self): return self._payment_id

    def set_method(self, m): self._method = m
    def get_method(self): return self._method

    def set_amount(self, a): self._amount = a
    def get_amount(self): return self._amount

    def set_status(self, s): self._status = s
    def get_status(self): return self._status

    def set_date(self, d): self._date = d
    def get_date(self): return self._date

    def display(self):
        print(f"Payment ID: {self._payment_id}, Method: {self._method}, Amount: {self._amount}, Status: {self._status}, Date: {self._date}")

# SingleRacePass Class - Represents a single race pass with seat and access info
class SingleRacePass:
    def __init__(self, race_name, date, seat_number, zone_access):
        try:
            self._race_name = race_name              # Name of the race
            self._date = date                        # Date of the race
            self._seat_number = seat_number          # Allocated seat number
            self._zone_access = zone_access          # Access zones (e.g., paddock, VIP area)
        except Exception as e:
            print(f"Error initializing SingleRacePass: {e}")

    def set_race_name(self, n): self._race_name = n
    def get_race_name(self): return self._race_name

    def set_date(self, d): self._date = d
    def get_date(self): return self._date

    def set_seat_number(self, s): self._seat_number = s
    def get_seat_number(self): return self._seat_number

    def set_zone_access(self, z): self._zone_access = z
    def get_zone_access(self): return self._zone_access

    def display(self):
        print(f"Race: {self._race_name}, Date: {self._date}, Seat: {self._seat_number}, Zone Access: {self._zone_access}")

# PurchaseOrder Class - Associated with multiple Tickets and one Payment
class PurchaseOrder:
    def __init__(self, order_id, customer_id, ticket_list, total_price, order_date, tickets=None, payment=None):
        try:
            self._order_id = order_id
            self._customer_id = customer_id
            self._ticket_list = ticket_list            # Raw ticket data list
            self._total_price = total_price
            self._order_date = order_date
            self._tickets = tickets if tickets is not None else []  # Initialize empty list if not passed
            self._payment = payment                    # ASSOCIATION: one Payment object
        except Exception as e:
            print(f"Error initializing PurchaseOrder: {e}")

    def set_order_id(self, id): self._order_id = id
    def get_order_id(self): return self._order_id

    def set_customer_id(self, cid): self._customer_id = cid
    def get_customer_id(self): return self._customer_id

    def set_ticket_list(self, tickets): self._ticket_list = tickets
    def get_ticket_list(self): return self._ticket_list

    def set_total_price(self, p): self._total_price = p
    def get_total_price(self): return self._total_price

    def set_order_date(self, d): self._order_date = d
    def get_order_date(self): return self._order_date

    def set_tickets(self, tk): self._tickets = tk
    def get_tickets(self): return self._tickets

    def set_payment(self, pm): self._payment = pm
    def get_payment(self): return self._payment

    def calculate_total(self):
        try:
            self._total_price = sum(ticket.get_price() for ticket in self._tickets)
            return self._total_price
        except Exception as e:
            print(f"Error calculating total: {e}")
            return 0

    def display(self):
        print(f"Order ID: {self._order_id}, Customer ID: {self._customer_id}, Total: {self._total_price}, Date: {self._order_date}")
        for ticket in self._tickets:
            ticket.display()
        if self._payment:
            self._payment.display()
