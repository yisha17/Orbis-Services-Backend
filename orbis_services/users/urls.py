from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


urlpatterns = [
    path('signup/', user_signup_view),
    path('auth/', custom_token_obtain),
    path('auth/refresh', jwt_views.token_refresh), 
    path('<int:id>/',user_detail_view),
]