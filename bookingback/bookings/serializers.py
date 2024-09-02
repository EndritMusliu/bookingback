from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'

class UserSerializer(WritableNestedModelSerializer):
    user_type = UserTypeSerializer()

    class Meta:
        model = User
        fields = '__all__'

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'

class CountrySerializer(WritableNestedModelSerializer):
    continent = ContinentSerializer()

    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(WritableNestedModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = '__all__'

class StreetSerializer(WritableNestedModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = '__all__'

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class PropertySerializer(WritableNestedModelSerializer):
    property_type = PropertyTypeSerializer()
    street = StreetSerializer()
    meal_offer = MealSerializer()

    class Meta:
        model = Property
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class FavoriteSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property = PropertySerializer()

    class Meta:
        model = Favorite
        fields = '__all__'

class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = '__all__'

class CategorySerializer(WritableNestedModelSerializer):
    category = CategoryTypeSerializer()
    property = PropertySerializer()

    class Meta:
        model = Category
        fields = '__all__'

class FeedbackSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property = PropertySerializer()

    class Meta:
        model = Feedback
        fields = '__all__'

class RoomSerializer(WritableNestedModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(WritableNestedModelSerializer):
    renter = UserSerializer()
    room = RoomSerializer()
    bank_details = serializers.PrimaryKeyRelatedField(queryset=BankDetails.objects.all(), required=False)

    class Meta:
        model = Booking
        fields = '__all__'

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = '__all__'

class RatingSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    property = PropertySerializer()

    class Meta:
        model = Rating
        fields = '__all__'

class FlightAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightAgency
        fields = '__all__'

class FlightStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightStatus
        fields = '__all__'

class FlightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightType
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class FlightSerializer(WritableNestedModelSerializer):
    flying_from = CitySerializer()
    flying_to = CitySerializer()
    flight_agency = FlightAgencySerializer()

    class Meta:
        model = Flight
        fields = '__all__'

class BookedFlightSerializer(WritableNestedModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()
    route = RouteSerializer()
    flight_status = FlightStatusSerializer()
    flight_type = FlightTypeSerializer()
    bank_account = serializers.PrimaryKeyRelatedField(queryset=BankDetails.objects.all(), required=False)

    class Meta:
        model = BookedFlight
        fields = '__all__'

class PriceSerializer(WritableNestedModelSerializer):
    flight = FlightSerializer()
    flight_type = FlightTypeSerializer()
    route = RouteSerializer()

    class Meta:
        model = Price
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class PropertyFeatureSerializer(WritableNestedModelSerializer):
    feature = FeatureSerializer()
    property = PropertySerializer()

    class Meta:
        model = PropertyFeature
        fields = '__all__'

class FeatureRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRoom
        fields = '__all__'

class RoomFeatureSerializer(WritableNestedModelSerializer):
    room = RoomSerializer()
    feature_room = FeatureRoomSerializer()

    class Meta:
        model = RoomFeature
        fields = '__all__'
