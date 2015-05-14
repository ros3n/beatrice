from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    address = serializers.CharField(max_length=None, min_length=None)
    location = serializers.CharField(max_length=64)
