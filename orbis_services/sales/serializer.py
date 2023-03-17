from rest_framework import serializers
from .models import Cars, UserReview, CarImages
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from users.serializer import UserReviewProfileSerializer


class CarReviewSerializer(SerializerExtensionsMixin,serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ('review_title','review_description','likes','views','car',)

        expandable_fields = dict(
            reviewer= UserReviewProfileSerializer,
        )    


class CarImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
        model = CarImages
        fields = ('image',)
        
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url)



class AllCarDetailSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Cars
        fields = ['id','car_brand','images']

    
    
class CarsSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(
        max_length=1000000, allow_empty_file=False, use_url=True), write_only=True)

    class Meta:
        model = Cars
        fields = '__all__'

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_car = Cars.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_car_image = CarImageSerializer.objects.create(product = new_car, images = uploaded_item)
        return new_car
    
class SalesVehicleSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
 
    def get_images(self, car):
       image = car.car_images.all()
       return  CarImageSerializer(instance=image, many=True,context=self.context).data 
    class Meta:
        model= Cars
        fields = '__all__'