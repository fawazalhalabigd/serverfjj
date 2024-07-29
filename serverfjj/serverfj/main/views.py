from django.shortcuts import render
from rest_framework import viewsets
 
# import local data
from .serializers import *
from .models import *
 
# Create your views here.



class IpsViewSet(viewsets.ModelViewSet):
    queryset = ips.objects.all()
    serializer_class = IpsSerializer

class MontagViewSet(viewsets.ModelViewSet):
    queryset = montag.objects.all()
    serializer_class = MontageSerializer

class MontageOrderViewSet(viewsets.ModelViewSet):
    queryset = montagOrder.objects.all()
    serializer_class = MontageOrderSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = EmployeeSerializer


class NotificateViewSet(viewsets.ModelViewSet):
    queryset = notificate.objects.all()
    serializer_class = NotificateSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = place.objects.all()
    serializer_class = PlaceSerializer

class MonyViewSet(viewsets.ModelViewSet):
    queryset = Mony.objects.all()
    serializer_class = MonySerializer

def jawad(request):
    return render(request,'jawad.html')