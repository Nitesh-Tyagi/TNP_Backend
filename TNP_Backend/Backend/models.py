from django.db import models

# Create your models here.

class TNPGuest(models.Model):
    FormID = models.BigAutoField(primary_key=True)
    DateCreated = models.DateTimeField()
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    CompanyName = models.CharField(max_length=50)
    HR_PhoneNo = models.CharField(max_length=10)
    HR_Email = models.CharField(max_length=30)
    NoRooms = models.IntegerField()
    NoMales = models.IntegerField()
    NoFemales = models.IntegerField()
    AOCheck = models.BooleanField()
    SupervisorCheck = models.BooleanField()
    VCCheck = models.BooleanField()
    Status = models.BooleanField()
    Comment = models.CharField(max_length=120)
    SentBack = models.BooleanField()

    class Meta:
        app_label = 'Backend'
        ordering = ['FormID']

class Hostel(models.Model):
    RoomID = models.BigAutoField(primary_key=True)
    RoomName = models.CharField(max_length=20)
    FloorName = models.CharField(max_length=20)
    Capacity = models.IntegerField()
    LastUsedDate = models.DateTimeField()
    LastOccupant = models.ForeignKey(TNPGuest, on_delete=models.SET_NULL, null=True)
    Status = models.BooleanField()

    class Meta:
        app_label = 'Backend'
        ordering = ['RoomID']

class Emails(models.Model):
    ID = models.IntegerField(primary_key=True)
    Email = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)

    class Meta:
        app_label = 'Backend'
        ordering = ['ID']
