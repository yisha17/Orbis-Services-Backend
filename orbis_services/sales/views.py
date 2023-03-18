from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions, authentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
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
        serializer =  CarReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)  
      
class UserReviewList(SerializerExtensionsAPIViewMixin,generics.ListAPIView):
    queryset = UserReview.objects.all()
    serializer_class = CarReviewSerializer
    permission_classes = [AllowAny,]
    lookup_field = 'car'
car_review_list = UserReviewList.as_view()


class FullDetailAboutSalesCar(generics.RetrieveAPIView):
    queryset = Cars.objects.all()
    serializer_class = SalesVehicleSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [AllowAny,]
    lookup_field = 'pk'
    
car_detail = FullDetailAboutSalesCar.as_view()

