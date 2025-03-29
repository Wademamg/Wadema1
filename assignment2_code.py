class Hotel:
    """Represents the hotel entity."""
    def __init__(self, hotel_name, location, phone_number, email, rating):
        self._hotelName = hotel_name
        self._location = location
        self._phoneNumber = phone_number
        self._email = email
        self._rating = rating

    def setHotelName(self, hotel_name):
        self._hotelName = hotel_name  # Set hotel name

    def getHotelName(self):
        return self._hotelName  # Return hotel name

    def setLocation(self, location):
        self._location = location  # Set location

    def getLocation(self):
        return self._location  # Return location

    def setPhoneNumber(self, phone_number):
        self._phoneNumber = phone_number  # Set phone number

    def getPhoneNumber(self):
        return self._phoneNumber  # Return phone number

    def setEmail(self, email):
        self._email = email  # Set email

    def getEmail(self):
        return self._email  # Return email

    def setRating(self, rating):
        self._rating = rating  # Set rating

    def getRating(self):
        return self._rating  # Return rating


class RoomType:
    """Represents a type of room in the hotel."""
    def __init__(self, type_name, occupancy, balcony, view):
        self._roomTypeName = type_name
        self._occupancy = occupancy
        self._balcony = balcony
        self._view = view

    def setRoomTypeName(self, type_name):
        self._roomTypeName = type_name  # Set room type name

    def getRoomTypeName(self):
        return self._roomTypeName  # Return room type name

    def setOccupancy(self, occupancy):
        self._occupancy = occupancy  # Set occupancy

    def getOccupancy(self):
        return self._occupancy  # Return occupancy

    def setBalcony(self, balcony):
        self._balcony = balcony  # Set balcony status

    def getBalcony(self):
        return self._balcony  # Return balcony status

    def setView(self, view):
        self._view = view  # Set room view

    def getView(self):
        return self._view  # Return room view


class Room(RoomType):
    """Room inherits from RoomType and adds specific details."""
    def __init__(self, room_number, is_available, price_per_night, amenities,
                 type_name, occupancy, balcony, view):
        super().__init__(type_name, occupancy, balcony, view)
        self._roomNumber = room_number
        self._isAvailable = is_available
        self._pricePerNight = price_per_night
        self._amenitiesList = amenities

    def setRoomNumber(self, room_number):
        self._roomNumber = room_number

    def getRoomNumber(self):
        return self._roomNumber

    def setIsAvailable(self, is_available):
        self._isAvailable = is_available

    def getIsAvailable(self):
        return self._isAvailable

    def setPricePerNight(self, price):
        self._pricePerNight = price

    def getPricePerNight(self):
        return self._pricePerNight

    def setAmenitiesList(self, amenities):
        self._amenitiesList = amenities

    def getAmenitiesList(self):
        return self._amenitiesList

    def calculateCost(self, days):
        return self._pricePerNight * days


class Guest:
    """Represents a hotel guest."""
    def __init__(self, guest_id, name, phone_number, email, loyalty_points):
        self._guestId = guest_id
        self._name = name
        self._phoneNumber = phone_number
        self._email = email
        self._loyaltyPoints = loyalty_points

    def setGuestId(self, guest_id):
        self._guestId = guest_id

    def getGuestId(self):
        return self._guestId

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setPhoneNumber(self, phone_number):
        self._phoneNumber = phone_number

    def getPhoneNumber(self):
        return self._phoneNumber

    def setEmail(self, email):
        self._email = email

    def getEmail(self):
        return self._email

    def setLoyaltyPoints(self, points):
        self._loyaltyPoints = points

    def getLoyaltyPoints(self):
        return self._loyaltyPoints


class Booking:
    """Handles a room booking."""
    def __init__(self, booking_id, check_in, check_out, total_cost, guest_id, room_id):
        self._bookingId = booking_id
        self._checkInDate = check_in
        self._checkOutDate = check_out
        self._totalCost = total_cost
        self._guestId = guest_id
        self._roomId = room_id

    def setBookingId(self, booking_id):
        self._bookingId = booking_id

    def getBookingId(self):
        return self._bookingId

    def setCheckInDate(self, check_in):
        self._checkInDate = check_in

    def getCheckInDate(self):
        return self._checkInDate

    def setCheckOutDate(self, check_out):
        self._checkOutDate = check_out

    def getCheckOutDate(self):
        return self._checkOutDate

    def setTotalCost(self, cost):
        self._totalCost = cost

    def getTotalCost(self):
        return self._totalCost

    def setGuestId(self, guest_id):
        self._guestId = guest_id

    def getGuestId(self):
        return self._guestId

    def setRoomId(self, room_id):
        self._roomId = room_id

    def getRoomId(self):
        return self._roomId


class Payment:
    """Handles booking payments."""
    def __init__(self, payment_id, method, amount, status, invoice_number, invoice_date, discount, additional_charges):
        self._paymentId = payment_id
        self._paymentMethod = method
        self._amount = amount
        self._status = status
        self._invoiceNumber = invoice_number
        self._invoiceDate = invoice_date
        self._discount = discount
        self._additionalCharges = additional_charges

    def setPaymentId(self, payment_id):
        self._paymentId = payment_id

    def getPaymentId(self):
        return self._paymentId

    def setPaymentMethod(self, method):
        self._paymentMethod = method

    def getPaymentMethod(self):
        return self._paymentMethod

    def setAmount(self, amount):
        self._amount = amount

    def getAmount(self):
        return self._amount

    def setStatus(self, status):
        self._status = status

    def getStatus(self):
        return self._status

    def setInvoiceNumber(self, number):
        self._invoiceNumber = number

    def getInvoiceNumber(self):
        return self._invoiceNumber

    def setInvoiceDate(self, date):
        self._invoiceDate = date

    def getInvoiceDate(self):
        return self._invoiceDate

    def setDiscount(self, discount):
        self._discount = discount

    def getDiscount(self):
        return self._discount

    def setAdditionalCharges(self, charges):
        self._additionalCharges = charges

    def getAdditionalCharges(self):
        return self._additionalCharges


class CustomerReview:
    """Handles customer reviews."""
    def __init__(self, review_id, review_date, rating, comments, guest_id):
        self._reviewId = review_id
        self._reviewDate = review_date
        self._rating = rating
        self._comments = comments
        self._guestId = guest_id

    def setReviewId(self, review_id):
        self._reviewId = review_id

    def getReviewId(self):
        return self._reviewId

    def setReviewDate(self, review_date):
        self._reviewDate = review_date

    def getReviewDate(self):
        return self._reviewDate

    def setRating(self, rating):
        self._rating = rating

    def getRating(self):
        return self._rating

    def setComments(self, comments):
        self._comments = comments

    def getComments(self):
        return self._comments

    def setGuestId(self, guest_id):
        self._guestId = guest_id

    def getGuestId(self):
        return self._guestId




