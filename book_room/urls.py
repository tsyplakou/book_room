"""
URL configuration for book_room project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from location.views import LocationViewSet
from room.views import RoomViewSet
from room_booking.views import BookingViewSet
from user.views import UserRegisterView, UserLoginView, UserLogoutView

default_router = DefaultRouter()
default_router.register('api/location', LocationViewSet, 'location')
default_router.register('api/room', RoomViewSet, 'room')
default_router.register('api/booking', BookingViewSet, 'booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),
    path('api/user/login/', UserLoginView.as_view(), name='user_login'),
    path('api/user/logout/', UserLogoutView.as_view(), name='user_logout'),
] + default_router.urls
