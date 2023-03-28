from rest_framework import serializers
from .models import TNPGuest, Hostel, Emails

class TNPGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNPGuest
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = '__all__'

class EmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = '__all__'
