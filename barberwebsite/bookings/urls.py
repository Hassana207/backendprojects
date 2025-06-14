from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booked_service, name='booked_service'),
    path('list/', views.booking_list, name='booking_list'),
]
