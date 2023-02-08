from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import *
from .models import *
from rest_framework import generics, permissions, authentication
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


user_signup_view = RegisterView.as_view()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
custom_token_obtain = MyTokenObtainPairView.as_view()


class UserDetailView(generics.RetrieveAPIView):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer