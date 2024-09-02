from django.db import models


class UserType(models.Model):
    ADMIN = 'ADMIN'
    USER = 'USER'
    BUSINESS = 'BUSINESS'
    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
        (BUSINESS, 'Business'),
    ]

    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, blank=True, null=True)


class User(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)


class Continent(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, blank=True, null=True)


class City(models.Model):
    city_name = models.CharField(max_length=150, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)


class Street(models.Model):
    street_name = models.CharField(max_length=150, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)


class PropertyType(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)


class Meal(models.Model):
    ALL_INCLUSIVE = 'ALL-INCLUSIVE'
    BREAKFAST_ONLY = 'BREAKFAST-ONLY'
    NO_MEAL_OFFER = 'NO MEAL OFFER'
    BREAKFAST_DINNER = 'BREAKFAST & DINNER'
    MEAL_CHOICES = [
        (ALL_INCLUSIVE, 'All-Inclusive'),
        (BREAKFAST_ONLY, 'Breakfast-Only'),
        (NO_MEAL_OFFER, 'No Meal Offer'),
        (BREAKFAST_DINNER, 'Breakfast & Dinner'),
    ]

    name = models.CharField(max_length=50, choices=MEAL_CHOICES, blank=True, null=True)


class Property(models.Model):
    property_name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, blank=True, null=True)
    meal_offer = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True, blank=True)
    check_in_hour = models.DateTimeField(blank=True, null=True)
    check_out_hour = models.DateTimeField(blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)


class CategoryType(models.Model):
    category = models.CharField(max_length=150, blank=True, null=True)


class Category(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)


class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_of_beds = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=150, blank=True, null=True)
    apartment_size = models.IntegerField(blank=True, null=True)
    room_description = models.TextField(blank=True, null=True)


class Booking(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_details = models.ForeignKey('BankDetails', on_delete=models.SET_NULL, null=True, blank=True)
    verified_by_owner = models.BooleanField(default=False)


class BankDetails(models.Model):
    account_name = models.CharField(max_length=150, blank=True, null=True)
    account_number = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)


class FlightAgency(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)


class FlightStatus(models.Model):
    IN_PROGRESS = 'IN PROGRESS'
    CURRENTLY_FLYING = 'CURRENTLY FLYING'
    CANCELLED = 'CANCELLED'
    DONE = 'DONE'
    FLIGHT_STATUS_CHOICES = [
        (IN_PROGRESS, 'In Progress'),
        (CURRENTLY_FLYING, 'Currently Flying'),
        (CANCELLED, 'Cancelled'),
        (DONE, 'Done'),
    ]

    name = models.CharField(max_length=50, choices=FLIGHT_STATUS_CHOICES, blank=True, null=True)


class FlightType(models.Model):
    ECONOMY = 'ECONOMY'
    BUSINESS = 'BUSINESS'
    PREMIUM_ECONOMY = 'PREMIUM ECONOMY'
    FLIGHT_TYPE_CHOICES = [
        (ECONOMY, 'Economy'),
        (BUSINESS, 'Business'),
        (PREMIUM_ECONOMY, 'Premium Economy'),
    ]

    name = models.CharField(max_length=50, choices=FLIGHT_TYPE_CHOICES, blank=True, null=True)


class Route(models.Model):
    ONE_WAY = 'ONE WAY'
    RETURN = 'RETURN'
    ROUTE_CHOICES = [
        (ONE_WAY, 'One Way'),
        (RETURN, 'Return'),
    ]

    name = models.CharField(max_length=50, choices=ROUTE_CHOICES, blank=True, null=True)


class Flight(models.Model):
    flight_no = models.IntegerField(blank=True, null=True)
    flying_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flying_from', blank=True, null=True)
    flying_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flying_to', blank=True, null=True)
    flight_agency = models.ForeignKey(FlightAgency, on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


class BookedFlight(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_account = models.ForeignKey(BankDetails, on_delete=models.SET_NULL, null=True, blank=True)
    flight_status = models.ForeignKey(FlightStatus, on_delete=models.CASCADE, blank=True, null=True)
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE, blank=True, null=True)


class Price(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)
    flight_type = models.ForeignKey(FlightType, on_delete=models.CASCADE, blank=True, null=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


class Feature(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)


class PropertyFeature(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=False)


class FeatureRoom(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)


class RoomFeature(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    feature_room = models.ForeignKey(FeatureRoom, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=False)
