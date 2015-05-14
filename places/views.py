from googleplaces import GooglePlaces
from googleplaces.types import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from places.serializers import LocationSerializer
from beatrice import settings

class LocationList(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, lat, lon, format=None):
        print lat, lon
        client = GooglePlaces(settings.GOOGLE_API_KEY)
        query_result = client.nearby_search(
            lat_lng={'lat': lat, 'lng': lon},
            radius=settings.PLACES_SEARCH_RADIUS,
            types=[
                TYPE_ACCOUNTING, TYPE_AIRPORT, TYPE_AMUSEMENT_PARK, TYPE_AQUARIUM, TYPE_ART_GALLERY, TYPE_ATM,
                TYPE_BAKERY, TYPE_BANK, TYPE_BAR, TYPE_BEAUTY_SALON, TYPE_BICYCLE_STORE, TYPE_BOOK_STORE,
                TYPE_BOWLING_ALLEY, TYPE_BUS_STATION, TYPE_CAFE, TYPE_CAMPGROUND, TYPE_CAR_DEALER, TYPE_CAR_RENTAL,
                TYPE_CAR_REPAIR, TYPE_CAR_WASH, TYPE_CASINO, TYPE_CEMETERY, TYPE_CHURCH, TYPE_CITY_HALL,
                TYPE_CLOTHING_STORE, TYPE_CONVENIENCE_STORE, TYPE_COURTHOUSE, TYPE_DENTIST, TYPE_DEPARTMENT_STORE,
                TYPE_DOCTOR, TYPE_ELECTRICIAN, TYPE_ELECTRONICS_STORE, TYPE_EMBASSY, TYPE_ESTABLISHMENT, TYPE_FINANCE,
                TYPE_FIRE_STATION, TYPE_FLORIST, TYPE_FOOD, TYPE_FUNERAL_HOME, TYPE_FURNITURE_STORE, TYPE_GAS_STATION,
                TYPE_GENERAL_CONTRACTOR, TYPE_GEOCODE, TYPE_GROCERY_OR_SUPERMARKET, TYPE_GYM, TYPE_HAIR_CARE,
                TYPE_HARDWARE_STORE, TYPE_HEALTH, TYPE_HINDU_TEMPLE, TYPE_HOME_GOODS_STORE, TYPE_HOSPITAL,
                TYPE_INSURANCE_AGENCY, TYPE_JEWELRY_STORE, TYPE_LAUNDRY, TYPE_LIBRARY, TYPE_LIQUOR_STORE,
                TYPE_LOCAL_GOVERNMENT_OFFICE, TYPE_LOCKSMITH, TYPE_LODGING, TYPE_MEAL_DELIVERY, TYPE_MEAL_TAKEAWAY,
                TYPE_MOSQUE, TYPE_MOVIE_RENTAL, TYPE_MOVIE_THEATER, TYPE_MOVING_COMPANY, TYPE_MUSEUM, TYPE_NIGHT_CLUB,
                TYPE_PAINTER, TYPE_PARK, TYPE_PARKING, TYPE_PET_STORE, TYPE_PHARMACY, TYPE_PHYSIOTHERAPIST,
                TYPE_PLACE_OF_WORSHIP, TYPE_PLUMBER, TYPE_POLICE, TYPE_POST_OFFICE, TYPE_REAL_ESTATE_AGENCY,
                TYPE_RESTAURANT, TYPE_ROOFING_CONTRACTOR, TYPE_RV_PARK, TYPE_SCHOOL, TYPE_SHOE_STORE,
                TYPE_SHOPPING_MALL, TYPE_SPA, TYPE_STADIUM, TYPE_STORAGE, TYPE_STORE, TYPE_SUBWAY_STATION,
                TYPE_SYNAGOGUE, TYPE_TAXI_STAND, TYPE_TRAIN_STATION, TYPE_TRAVEL_AGENCY, TYPE_UNIVERSITY,
                TYPE_VETERINARY_CARE, TYPE_ZOO
            ]
        )
        result = []
        if query_result:
            for place in query_result.places:
                place.get_details()
                data = {
                    'name': place.name,
                    'address': place.formatted_address,
                    'location': place.geo_location,
                }

                result.append(data)
            serializer = LocationSerializer(result, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_200_OK)
