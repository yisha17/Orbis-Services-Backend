from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('<int:pk>/',get_sales_vehicle_info),
    path('review/<int:car>/',user_review_list),
    path('detail/<int:pk>/',car_detail),
]