import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Destination, Reservation
from .serializer import DestinationSerializer, ReservationSerializer

# Create your views here.
@api_view(['GET'])
def getDestinations(request):
    app = Destination.objects.all()
    serializer = DestinationSerializer(app, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def postDestination(request):
    newDestination = Destination(
        title=request.data['title'],
        description=request.data['description'],
        location=request.data['location'],
        pricePerNight=request.data['pricePerNight'],
        totalSpots=request.data['totalSpots'],
        sale=request.data['sale'])
    newDestination.save()

    return Response(newDestination.name)

@api_view(['PUT'])
def updateDestination(request, pk):
    destination = Destination.objects.get(id=pk)

    if (destination == None):
        return Response(status=404)

    destination.title = request.data['title']
    destination.description = request.data['description']
    destination.location = request.data['location']
    destination.pricePerNight = request.data['pricePerNight']
    destination.totalSpots = request.data['totalSpots']
    destination.sale = request.data['sale']
    destination.save()

    return Response(destination.name)

@api_view(['DELETE'])
def deleteDestination(pk):
    destination = Destination.objects.get(id=pk)

    if (destination == None):
        return Response(status=404)

    destination.delete()

    return Response(destination.name)


@api_view(['GET'])
def getReservations():
    app = Reservation.objects.all()
    serializer = ReservationSerializer(app, many=True)

    return Response(serializer.data)

# params: destination, checkIn, checkOut
@api_view(['POST'])
def postReservation(request):
    checkIn = datetime.datetime.fromisoformat(request.data['checkIn']).date()
    checkOut = datetime.datetime.fromisoformat(request.data['checkOut']).date()
    print(checkIn)
    print(checkOut)
    print((checkOut - checkIn).days)
    destination = Destination.objects.get(id=request.data['destinationId'])
    totalPrice = destination.pricePerNight * (checkOut - checkIn).days
    print(totalPrice)

    newReservation = Reservation(
        destination=destination,
        checkIn=checkIn,
        checkOut=checkOut,
        totalPrice=totalPrice)
    newReservation.save()

    destination.save()

    return Response()

# params: destination, checkIn, checkOut
@api_view(['POST'])
def checkAvailability(request):
    destination = Destination.objects.get(id=request.data['destinationId'])
    reservations = Reservation.objects.filter(destination=destination)
    checkIn = datetime.datetime.fromisoformat(request.data['checkIn']).date()
    checkOut = datetime.datetime.fromisoformat(request.data['checkOut']).date()

    occupiedSpotsInPeriod = 0

    for reservation in reservations:
        if (checkIn >= reservation.checkIn and checkIn <= reservation.checkOut) or (checkOut >= reservation.checkIn and checkOut <= reservation.checkOut):
            occupiedSpotsInPeriod += 1

    if (destination.totalSpots - occupiedSpotsInPeriod <= 0):
        return Response(False)
    return Response(True)


@api_view(['POST'])
def getAvailableDestinationsInPeriod(request):
    checkIn = datetime.datetime.fromisoformat(request.data['checkIn']).date()
    checkOut = datetime.datetime.fromisoformat(request.data['checkOut']).date()
    print(checkIn)
    availableDestinations = []

    for destination in Destination.objects.all():
        reservations = Reservation.objects.filter(destination=destination)
        occupiedSpotsInPeriod = 0

        for reservation in reservations:
            reservation_checkIn = reservation.checkIn
            reservation_checkOut = reservation.checkOut

            if (checkIn >= reservation_checkIn and checkIn <= reservation_checkOut) or \
            (checkOut >= reservation_checkIn and checkOut <= reservation_checkOut):
                occupiedSpotsInPeriod += 1

        if (destination.totalSpots - occupiedSpotsInPeriod > 0):
            availableDestinations.append(destination)

    serializer = DestinationSerializer(availableDestinations, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def getReservationsForDestination(request, pk):
    destination = Destination.objects.get(id=pk)
    reservations = Reservation.objects.filter(destination=destination)
    serializer = ReservationSerializer(reservations, many=True)

    return Response(serializer.data)