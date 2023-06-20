from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrdersSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .serializers import MedicinesSerializer,SliderSerializer,ImageSerializer
from .models import Medicines,Slider,UploadPrescription
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
class ImageUploadView(CreateAPIView):
    queryset = UploadPrescription.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]
class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicinesPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class MedicinesListView(generics.ListAPIView):
    queryset = Medicines.objects.all()
    serializer_class = MedicinesSerializer
    pagination_class = MedicinesPagination
    search_param = 'search'
    def get_queryset(self):
        queryset = Medicines.objects.all()

        # Perform search if query parameter is provided
        query = self.request.query_params.get('search')
        if query:
            queryset = queryset.filter(name__icontains=query) | queryset.filter(salt__icontains=query)

        return queryset

class SlidersListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
