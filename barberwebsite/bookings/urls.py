from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.booked_service, name='booked_service'),
    path('all_bookings/', views.booking_list, name='booking_list'),
    path('my_bookings/',views.user_booking_list,name="user_booking_list"),
    path('reschedule/<int:id>/',views.reschedule_booking,name="reschedule_date"),
    path('cancel/<int:id>/',views.cancel_booking,name="cancel_booking"),
     path('dashboard/', views.customer_dashboard, name='customerDashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='adminDashBoard'),
    path('success/',views.success_page,name='sucess-page')
]
