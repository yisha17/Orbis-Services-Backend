from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, authentication
from .models import *
from .serializer import *
# Create your views here.


@api_view(['GET',])
def get_sales_vehicle_info(request,pk):
    try:
        car = Cars.objects.get(pk=pk)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =  CarsSerializer(car)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET',])
def get_user_review(request,car):
    try:
        review = UserReview.objects.get(pk=car)
    except Cars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =  UserReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)    


class UserReviewList(generics.ListAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    lookup_field = 'car'
user_review_list = UserReviewList.as_view()


class FullDetailAboutSalesCar(generics.RetrieveAPIView):
    queryset = CarImages.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pk'
car_detail = FullDetailAboutSalesCar.as_view()