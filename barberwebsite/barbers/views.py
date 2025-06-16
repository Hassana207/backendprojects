from django.shortcuts import render , redirect , get_object_or_404
from .forms import SetBarberInfo ,RateBarberService
from .models import BarberInfo

# Create your views here.
def barber_information(request):
    if request.method == "POST":
        form = SetBarberInfo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('barber_success_page')
        
    else:
        form = SetBarberInfo()
    return render(request,"barber_information.html",{'form':form})

def rate_barber_service(request,barber_id):
   barber = BarberInfo.objects.get(id=barber_id)

   if request.method == "POST":
        form = RateBarberService(request.POST, instance=barber)
        if form.is_valid():
            form.save()
            return redirect('rate_success_page')  
   else:
        form = RateBarberService(instance=barber)

   return render(request, "rate_barber_service.html", {'form': form, 'barber': barber})

def edit_barber_information(request,barber_id):
   barber = get_object_or_404(BarberInfo, id=barber_id)

   if request.method == "POST":
        form = SetBarberInfo(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            form.save()
            return redirect('barber_success_page')  
   else:
        form = SetBarberInfo(instance=barber)

   return render(request, "edit_barber_information.html", {"form": form})

def delete_barber(request,barber_id):
    barber = get_object_or_404(BarberInfo, id=barber_id)
    if request.method == "POST":
        barber.delete()
        return redirect ('delete_sucess_page')
    return render(request,"delete_barber.html",{'barber':barber})

def barber_success_page(request):
    return render(request,"barber_success_page.html")

def rate_success_page(request):
    return render(request,"rate_success_page.html")

def delete_success_page(request):
    return render(request,"delete_success_page.html")


