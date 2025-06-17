from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('information/', views.barber_information, name="barber_information"),
    path('rateBarber/<int:barber_id>/', views.rate_barber_service, name='rate_barber_service'),
    path('editBarber/<int:barber_id>/', views.edit_barber_information, name='edit_barber_information'),
    path('deleteBarber/<int:barber_id>/', views.delete_barber, name='delete_barber'),
    path('success/', views.barber_success_page, name='barber_success_page'),
    path('rate-success/', views.rate_success_page, name='rate_success_page'),
    path('delete-success/', views.delete_success_page, name='delete_success_page'),
    path('profile/', views.barber_profile, name="barber_profile"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
