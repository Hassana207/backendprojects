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
    path('success/',views.success_page,name='success-page'),
    path('successReschedule/',views.success_reschedule_page,name='reschedule_page_success'),
    path('cancelsuccesspage/',views.cancel_success_page,name='cancel_success_page'),
]
