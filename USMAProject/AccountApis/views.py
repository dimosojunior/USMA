from django.shortcuts import render,redirect


# Create your views here.
from django.shortcuts import render,get_object_or_404
from Apis.serializers import *
from USMAApp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Apis.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

# 	def get(self,request, format=None):
# 		return Response("User Account View", status=200)

# 	def post(self,request, format=None):

# 		return Response("Creating User", status=200)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# SIGNIN YA KAWAIDA SIO YA APIS
def signin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid, Username or Password is incorrect')
            return redirect('home')

    else:
        return render(request, 'USMAApp/home.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


# SIGNUP YA KAWAIDA SIO YA APIS
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('home')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('home')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()



                #log user in and redirect to settings page
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)

                messages.success(request, f'You have registered successfully as {username} ')
                return redirect('home')

                
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('home')

    # else:
    #     return render(request, 'USMAApp/home.html')



# SIGNUP YA APIS
class user_create_view(generics.GenericAPIView):
    serializer_class=UserCreationSerializer

    @swagger_auto_schema(operation_summary="User Registration Form")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)









