from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TNPGuest, Hostel, Emails
from .serializers import TNPGuestSerializer, HostelSerializer, EmailsSerializer

class TNPGuestList(generics.ListCreateAPIView):
    queryset = TNPGuest.objects.all()
    serializer_class = TNPGuestSerializer

class TNPGuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TNPGuest.objects.all()
    serializer_class = TNPGuestSerializer

class HostelList(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class HostelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class EmailsList(generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer

class EmailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer
