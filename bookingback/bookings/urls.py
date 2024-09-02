from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usertypes', UserTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'continents', ContinentViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'streets', StreetViewSet)
router.register(r'propertytypes', PropertyTypeViewSet)
router.register(r'meals', MealViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'categorytypes', CategoryTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'bankdetails', BankDetailsViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'flightagencies', FlightAgencyViewSet)
router.register(r'flightstatuses', FlightStatusViewSet)
router.register(r'flighttypes', FlightTypeViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'bookedflights', BookedFlightViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'propertyfeatures', PropertyFeatureViewSet)
router.register(r'featurerooms', FeatureRoomViewSet)
router.register(r'roomfeatures', RoomFeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
