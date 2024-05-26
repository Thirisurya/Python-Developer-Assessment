from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
from django.shortcuts import get_object_or_404
import requests

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Data Pusher App!")

def home(request):
    return render(request, 'home.html')

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class AccountDestinationsView(APIView):
    def get(self, request, account_id):
        account = get_object_or_404(Account, account_id=account_id)
        destinations = account.destinations.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

class IncomingDataView(APIView):
    def post(self, request):
        token = request.headers.get('CL-X-TOKEN')
        if not token:
            return Response({'error': 'Un Authenticate'}, status=status.HTTP_401_UNAUTHORIZED)

        account = get_object_or_404(Account, app_secret_token=token)
        data = request.data

        for destination in account.destinations.all():
            headers = destination.headers
            url = destination.url
            method = destination.http_method

            if method == 'GET':
                response = requests.get(url, headers=headers, params=data)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)

            if response.status_code != 200:
                return Response({'error': 'Failed to send data'}, status=response.status_code)

        return Response({'status': 'Data sent successfully'}, status=status.HTTP_200_OK)
