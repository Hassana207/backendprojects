from django.shortcuts import render, redirect ,get_object_or_404
from .forms import BookingForm
from django.core.mail import send_mail
from .models import Booking
from django.conf import settings
from django.utils.dateparse import parse_datetime

def booked_service(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booked_session = form.save(commit=False)
            booked_session.customer = request.user
            booked_session.save()
            form.save_m2m()

            # Email content
            subject = "Booking Confirmation"
            services = ', '.join([s.name for s in booked_session.services.all()])
            barber = booked_session.barber.name
            message_body = (
                f"Hello {booked_session.name},\n\n"
                f"Your booking for {services} with {barber} on {booked_session.date} has been received."
            )

            # Send email to customer
            send_mail(
                subject,
                message_body,
                settings.DEFAULT_FROM_EMAIL,
                [booked_session.email]
            )

            # Send email to admin
            send_mail(
                "New booking",
                f"Booking from {booked_session.name} ({booked_session.email})",
                settings.DEFAULT_FROM_EMAIL,
                ["ayindehassan776@gmail.com"]
            )

            return redirect("success-page")
    else:
        form = BookingForm()

    return render(request, "book_services.html", {"form": form})

def booking_list(request):
    all_sessions = Booking.objects.all()
    return render(request, "booking_list.html", {'book_list': all_sessions})


def user_booking_list(request):
    user_sessions = Booking.objects.filter(customer=request.user)
    return render(request, "user_booking_list.html", {'book_list': user_sessions})

def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id, customer=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect("user_booking_list")

    return render(request, "cancel_booking.html", {"booking": booking})

def reschedule_booking(request,id):
     booking = get_object_or_404(Booking,id=id,customer = request.user)

     if request.method == "POST":
        new_date_str = request.POST.get('new_date')  
        new_date = parse_datetime(new_date_str)
        if new_date.is_valid():
             booking.date = new_date
             booking.save()

             subject = "Booking Rescheduled"
             message_body = (
                f"Your booking with {booking.barber} has been rescheduled to {booking.date}. Thanks!"
            )
             send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [booking.email])
             send_mail(subject, f"{booking.name} has rescheduled to {booking.date}",
                      settings.DEFAULT_FROM_EMAIL, ["ayindehassan776@gmail.com"])

             return redirect("user_booking_list")  
        else:
            
            pass

    
     return render(request, "reschedule_booking.html", {"booking": booking})

def customer_dashboard(request):
    return render(request, "customer_dashboard.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")