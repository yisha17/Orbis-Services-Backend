from rest_framework import serializers
from .models import Cars,UserReview,CarImages


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'
        

class CarsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Cars
        fields = '__all__'
        
       

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ['cars','image']
        depth= 1        