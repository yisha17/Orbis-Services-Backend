from rest_framework import serializers
from .models import Cars, UserReview, CarImages


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = '__all__'


class CarImageSerializer(serializers.ModelSerializer):
    car_image = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
        model = CarImages
        fields = ['car_image']
        
    def get_photo_url(self, car):
        request = self.context.get('request')
        car_image = car.photo.url
        return request.build_absolute_uri(car_image)



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