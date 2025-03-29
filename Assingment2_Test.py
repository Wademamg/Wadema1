from datetime import datetime
from assignment2_code import Hotel, Room, RoomType, Guest, Booking, Payment, CustomerReview

# Setup hotel, rooms, guests, bookings

# Hotel info
hotel = Hotel("Royal Stay", "Abu Dhabi", "+971-123-5678", "royal@stay.com", 4.6)

# Room info
room1 = Room("20", True, 320.0, ["jacuzzi", "king bed"], "Suite", 3, True, "Sea View")
room2 = Room("21", True, 180.0, ["TV", "WiFi", "mini fridge"], "Standard", 2, False, "City View")

# Display hotel details

print("\n - HOTEL INFORMATION")
print("Hotel Name:", hotel.getHotelName())
print("Location:", hotel.getLocation())
print("Phone:", hotel.getPhoneNumber())
print("Email:", hotel.getEmail())
print("Rating:", hotel.getRating())

# Display room details
print("\n - ROOM DETAILS ")
for room in [room1, room2]:
    print(f"\nRoom Number: {room.getRoomNumber()}")
    print("Price/Night:", room.getPricePerNight())
    print("Available:", room.getIsAvailable())
    print("Room Type:", room.getRoomTypeName())
    print("Occupancy:", room.getOccupancy())
    print("Balcony:", room.getBalcony())
    print("View:", room.getView())
    print("Amenities:", room.getAmenitiesList())

# Create a guest

guest = Guest("G002", "Meera", "+971-555-6789", "meera@example.com", 3)

print("\n- GUEST CREATED")
print("Guest ID:", guest.getGuestId())
print("Name:", guest.getName())
print("Phone Number:", guest.getPhoneNumber())
print("Email:", guest.getEmail())
print("Loyalty Points:", guest.getLoyaltyPoints())

# Make a booking

checkin = "2025-06-10"
checkout = "2025-06-15"
days = (datetime.strptime(checkout, "%Y-%m-%d") - datetime.strptime(checkin, "%Y-%m-%d")).days
cost = room2.getPricePerNight() * days

booking = Booking("B002", checkin, checkout, cost, guest.getGuestId(), room2.getRoomNumber())

print("\n- BOOKING CONFIRMED")
print("Booking ID:", booking.getBookingId())
print("Guest ID:", booking.getGuestId())
print("Room Number:", booking.getRoomId())
print("Check-in:", booking.getCheckInDate())
print("Check-out:", booking.getCheckOutDate())
print("Total Cost:", booking.getTotalCost())

# Make a payment

invoice_date = datetime.now().strftime("%Y-%m-%d")
payment = Payment("P002", "Debit Card", cost, "Completed", "INV200", invoice_date, 15.0, 10.0)


print("\n- PAYMENT DETAILS")
print("Payment ID:", payment.getPaymentId())
print("Method:", payment.getPaymentMethod())
print("Amount:", payment.getAmount())
print("Status:", payment.getStatus())
print("Invoice No:", payment.getInvoiceNumber())
print("Invoice Date:", payment.getInvoiceDate())
print("Discount:", payment.getDiscount())
print("Additional Charges:", payment.getAdditionalCharges())

# Submit a review

review = CustomerReview("R002", "2025-06-16", 4.5, "Clean room and helpful staff!", guest.getGuestId())

print("\n- CUSTOMER REVIEW")
print("Review ID:", review.getReviewId())
print("Date:", review.getReviewDate())
print("Rating:", review.getRating())
print("Comment:", review.getComments())





