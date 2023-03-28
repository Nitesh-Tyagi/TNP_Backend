from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
from .models import TNPGuest, Hostel, Emails
from .serializers import TNPGuestSerializer, HostelSerializer, EmailsSerializer

# class TNPGuestList(generics.ListCreateAPIView):
#     queryset = TNPGuest.objects.all()
#     serializer_class = TNPGuestSerializer

# class TNPGuestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TNPGuest.objects.all()
#     serializer_class = TNPGuestSerializer

# class HostelList(generics.ListCreateAPIView):
#     queryset = Hostel.objects.all()
#     serializer_class = HostelSerializer

# class HostelDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hostel.objects.all()
#     serializer_class = HostelSerializer

# class EmailsList(generics.ListCreateAPIView):
#     queryset = Emails.objects.all()
#     serializer_class = EmailsSerializer

# class EmailsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Emails.objects.all()
#     serializer_class = EmailsSerializer

@api_view(['GET'])
def getForms(request):
    userId = request.GET.get('userId')
    status = request.GET.get('status')
    queryset = TNPGuest.objects.all()

    if userId == '1' and status == '0':
        queryset = queryset.filter(VCCheck=0)
    elif userId == '1' and status == '1':
        queryset = queryset.filter(VCCheck=1)
    elif userId == '2' and status == '0':
        queryset = queryset.filter(AOCheck=0)
    elif userId == '2' and status == '1':
        queryset = queryset.filter(AOCheck=1)
    elif userId == '3' and status == '0':
        queryset = queryset.filter(AOCheck=1, SupervisorCheck=0)
    elif userId == '3' and status == '1':
        queryset = queryset.filter(SupervisorCheck=1)
    elif userId == '4' and status == '0':
        queryset = queryset.filter(SupervisorCheck=1, VCCheck=0)
    elif userId == '4' and status == '1':
        queryset = queryset.filter(VCCheck=1)

    serializer = TNPGuestSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getForm(request, formId):
    queryset = TNPGuest.objects.filter(FormID=formId)
    serializer = TNPGuestSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postForm(request):
    serializer = TNPGuestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def putForm(request, formId):
    try:
        instance = TNPGuest.objects.get(FormID=formId)
    except TNPGuest.DoesNotExist:
        return Response(status=404)

    serializer = TNPGuestSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delForm(request, formId):
    try:
        instance = TNPGuest.objects.get(FormID=formId)
    except TNPGuest.DoesNotExist:
        return Response(status=404)

    instance.delete()
    return Response(status=204)
