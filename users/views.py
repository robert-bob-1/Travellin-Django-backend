from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import ClientSerializer, AgentSerializer
from .models import Client, Agent
# Create your views here.

@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    if Client.objects.filter(username=username, password=password).exists():
        return Response('client')
    elif Agent.objects.filter(username=username, password=password).exists():
        return Response('agent')
    else:
        return Response(status=404)

@api_view(['POST'])
def postClient(request):
    newClient = Client(username=request.data['username'], password=request.data['password'], phone_number=request.data['phoneNumber'])
    newClient.save()

    return Response(newClient.username)

@api_view(['POST'])
def postAgent(request):
    newAgent = Agent(username=request.data['username'], password=request.data['password'], company_name=request.data['companyName'])
    newAgent.save()

    return Response(newAgent.username)
