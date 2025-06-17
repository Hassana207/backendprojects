from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceForm
from .models import Service


def set_service_information(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_success_page")
    else:
        form = ServiceForm()
    return render(request, "set_service_information.html", {"form": form})


def edit_service_information(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("service_success_page")
    else:
        form = ServiceForm(instance=service)
    return render(request, "set_service_information.html", {"form": form})

def service_success_page(request):
    return render(request,"service_success_page.html")
