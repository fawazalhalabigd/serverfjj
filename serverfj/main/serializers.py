from rest_framework import serializers
 
# import model from models.py
from .models import *
 
# Create a model serializer
class IpsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = ips
        fields = ('ip', 'description')


class MontageSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = montag
        fields = "__all__"


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = place
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = employee
        fields = "__all__"

class NotificateSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = notificate
        fields = "__all__"

class MonySerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Mony
        fields = "__all__"