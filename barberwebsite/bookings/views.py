from django.shortcuts import render, redirect ,get_object_or_404
from .forms import BookingForm
from django.core.mail import send_mail
from .models import Booking
from django.conf import settings
from django.utils.dateparse import parse_datetime
from barbers.models import BarberInfo


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
                f"Hello {booked_session.name},\n\n\n\n\n\n\n\n\n"
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
                f"Booking from {booked_session.name} ({booked_session.email}) on the {booked_session.date}",
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

from django.core.mail import send_mail
from django.conf import settings

def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == "POST":
        
        customer_email = booking.email
        customer_name = booking.name
        barber = booking.barber
        date = booking.date

        
        booking.delete()

        
        subject_customer = "Booking Cancelled"
        message_customer = (
            f"Hello {customer_name},\n\n"
            f"Your booking with {barber.name} on {date} has been cancelled.\n"
            "Thank you for using Ace Barbershop."
        )
        send_mail(subject_customer, message_customer, settings.DEFAULT_FROM_EMAIL, [customer_email])

        
        subject_admin = f"Booking Cancelled by {customer_name}"
        message_admin = (
            f"{customer_name} has cancelled their booking with {barber.name} scheduled on {date}."
        )
        send_mail(subject_admin, message_admin, settings.DEFAULT_FROM_EMAIL, ["ayindehassan776@gmail.com"])

        return redirect("cancel_success_page")

    return render(request, "cancel_booking.html", {"booking": booking})

def reschedule_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == "POST":
        new_date_str = request.POST.get('new_date')

        if new_date_str:  
            new_date = parse_datetime(new_date_str)

            if new_date:
                booking.date = new_date
                booking.save()

                subject = "Booking Rescheduled"
                message_body = (
                    f"Your booking with {booking.barber} has been rescheduled to {booking.date}. Thanks!"
                )

                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [booking.email])
                send_mail(subject, f"{booking.name} has rescheduled to {booking.date}",
                          settings.DEFAULT_FROM_EMAIL, ["ayindehassan776@gmail.com"])

                return redirect("reschedule_page_success")
            else:
                
                return render(request, "reschedule_booking.html", {
                    "booking": booking,
                    "error": "Invalid date format. Please enter a valid date."
                })

        else:
            
            return render(request, "reschedule_booking.html", {
                "booking": booking,
                "error": "Please select a new date."
            })

    return render(request, "reschedule_booking.html", {"booking": booking})

def customer_dashboard(request):
    barbers = BarberInfo.objects.all()
    return render(request, 'customer_dashboard.html', {'barbers': barbers})

def admin_dashboard(request):
    barbers = BarberInfo.objects.all()
    return render(request, 'admin_dashboard.html', {'barbers': barbers})


def success_page(request):
    return render(request,"success_page.html")

def success_reschedule_page(request):
    return render(request,"success_reschedule_page.html")


def cancel_success_page(request):
 return render(request,"cancel_success_page.html")