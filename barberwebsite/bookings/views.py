from django.shortcuts import render, redirect
from .forms import BookingForm
from django.core.mail import send_mail
from .models import Booking
from django.conf import settings

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
        return render(request,"booking_list.html",{'book_list',all_sessions})

def user_booking_list(request):
    user_sessions = Booking.objects.filter(customer=request.user)
    return render(request, "user_booking_list.html", {'book_list': user_sessions})

