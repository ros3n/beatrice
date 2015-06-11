from googleplaces import GooglePlaces
from googleplaces.types import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from places.serializers import LocationSerializer
from beatrice import settings

from tasks.models import Task

class LocationList(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, lat, lon, format=None):
        print lat, lon
        client = GooglePlaces(settings.GOOGLE_API_KEY)
        query_result = client.nearby_search(
            lat_lng={'lat': lat, 'lng': lon},
            radius=settings.PLACES_SEARCH_RADIUS,
            types=[
                TYPE_ATM, TYPE_BAKERY, TYPE_BANK, TYPE_BOOK_STORE,
                TYPE_CAR_WASH, TYPE_CLOTHING_STORE,TYPE_ELECTRONICS_STORE,
                TYPE_FLORIST, TYPE_FOOD, TYPE_GROCERY_OR_SUPERMARKET,
                TYPE_HARDWARE_STORE, TYPE_LIQUOR_STORE, TYPE_PHARMACY,
                TYPE_SHOPPING_MALL, TYPE_CONVENIENCE_STORE,
            ]
        )

        result = []
        if query_result:
            for place in query_result.places:
                place.get_details()

                tasks = Task.objects.filter(category__code__in=place.types)

                if tasks:
                    data = {
                        'name': place.name,
                        'address': place.formatted_address,
                        'location': place.geo_location,
                        'tasks': ";".join(map(lambda x: str(x.id), tasks))
                    }

                    result.append(data)
            serializer = LocationSerializer(result, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_200_OK)
