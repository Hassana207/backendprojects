from django.urls import path
from . import views

urlpatterns = [
    path("service/information", views.set_service_information, name="set_service_information"),
    path("edit/service/<int:service_id>/", views.edit_service_information, name="edit_service_information"),
    path("service/success/", views.service_success_page, name="service_success_page"),
    path('services/', views.service_list, name='service_list'),
    path('services/delete/<int:service_id>/', views.delete_service_information, name='delete_service_information'),
    path('services/delete/success/', views.delete_successful, name='delete_successful'),
]
