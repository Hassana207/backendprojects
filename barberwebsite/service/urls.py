from django.urls import path
from . import views

urlpatterns = [
    path("service/information", views.set_service_information, name="set_service_information"),
    path("edit/service/<int:service_id>/", views.edit_service_information, name="edit_service_information"),
    path("service/success/", views.service_success_page, name="service_success_page"),
]
