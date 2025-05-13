
from UMLCode import Event, Ticket, Payment, PurchaseOrder, Customer, Admin, User, SeasonMembership, SingleRacePass

# ----------------- TEST CASE (Same format as hotel project) -----------------
if __name__ == "__main__":
    from datetime import datetime

    # Test Run 1
    print("\n--- GRAND PRIX SYSTEM: TEST RUN 1 ---")

    # Create Event
    event1 = Event("EV100", "Abu Dhabi GP", "2025-12-05", "Yas Marina", "Final race of the season")

    # Create Tickets (Composition)
    ticket1 = Ticket("TK1001", "VIP", 1500.0, "2025-12-05", "VIP Paddock + Pit Walk", event1)
    ticket2 = Ticket("TK1002", "General", 500.0, "2025-12-05", "Main Grandstand", event1)

    # Create SingleRacePass
    srp = SingleRacePass("Abu Dhabi GP", "2025-12-05", "A10", "Paddock")

    # Create Payment
    payment1 = Payment("PM1001", "Credit Card", 0.0, "Pending", datetime.now().strftime("%Y-%m-%d"))

    # Create Purchase Order
    order1 = PurchaseOrder("PO1001", "CU001", ["TK1001", "TK1002"], 0.0, "2025-11-30", [ticket1, ticket2], payment1)
    total1 = order1.calculate_total()
    payment1.set_amount(total1)
    payment1.set_status("Completed")

    # Create Customer
    customer1 = Customer("CU001", "Wadeema", "wadema@example.com", "secure123", "customer", 120, "0501112233", "Abu Dhabi", [order1])

    # Display
    customer1.display()
    print("\n- Single Race Pass -")
    srp.display()

    # Test Run 2
    print("\n--- GRAND PRIX SYSTEM: TEST RUN 2 ---")

    event2 = Event("EV200", "Dubai GP", "2026-03-22", "Dubai Street Circuit", "Opening race of the new season")
    ticket3 = Ticket("TK2001", "Premium", 950.0, "2026-03-22", "Premium Seats + Free Shuttle", event2)

    payment2 = Payment("PM2001", "Apple Pay", 0.0, "Pending", datetime.now().strftime("%Y-%m-%d"))

    order2 = PurchaseOrder("PO2001", "CU002", ["TK2001"], 0.0, "2026-03-01", [ticket3], payment2)
    total2 = order2.calculate_total()
    payment2.set_amount(total2)
    payment2.set_status("Completed")

    customer2 = Customer("CU002", "Salem", "salem@example.com", "pass456", "customer", 75, "0523344556", "Dubai", [order2])

    customer2.display()
