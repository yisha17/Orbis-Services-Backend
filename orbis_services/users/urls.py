from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('api/users/', user_signup_view),
    path('api/auth/', custom_token_obtain),
    path('api/auth/refresh', jwt_views.token_refresh), 
]