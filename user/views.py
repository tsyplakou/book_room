from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class UserLogoutView(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self,request):
        logout(request)
        return Response({"message":"logout"}, status=status.HTTP_200_OK)
    

class UserLoginView(APIView):
    def post(self, requset):   
        serializer = UserLoginSerializer(data=requset.data)
        if serializer.is_valid():
            token = serializer.save()
            return Response({'token': token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserRegisterView(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = []

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

