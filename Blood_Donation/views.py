from django.shortcuts import render, redirect
from .forms import DonorForm, CustomerForm
from .models import Donor,Request_Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required()
def donor_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DonorForm()
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(instance=donor)
        return render(request, "Blood_Donation/donorform.html", {'form': form})
    else:
        if id == 0:
            form = DonorForm(request.POST)
        else:
            donor = Donor.objects.get(pk=id)
            form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('/donation/donorsuccess/')
        else:
            return render(request, "Blood_Donation/donorform.html", {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def donor_list(request):
    context = {'donor_list': Donor.objects.all()}
    return render(request, 'Blood_Donation/donorlist.html', context)


def customer_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            donor = Request_Customer.objects.get(pk=id)
            form = CustomerForm(instance=donor)
        return render(request, "Blood_Donation/customerform.html", {'form': form})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            donor = Request_Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('/donation/customersuccess/')
        else:
            return render(request, "Blood_Donation/customerform.html", {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def customer_list(request):
    context = {'customer_list': Request_Customer.objects.all()}
    return render(request, 'Blood_Donation/customerlist.html', context)

def donor_delete(request,id):
    donor = Donor.objects.get(pk=id)
    donor.delete()
    return redirect('/donation/donorlist/')

def customer_delete(request,id):
    customer = Request_Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/donation/customerlist/')
    
def donor_success(request):
    return render(request,'Blood_Donation/donorsuccess.html')    

def customer_success(request):
    return render(request,'Blood_Donation/customersuccess.html')    

def donor_home(request):
    return render(request,'Blood_Donation/home.html')

def choice(request):
    return render(request,'Blood_Donation/choice.html')

def contactus(request):
    return render(request,'Blood_Donation/contactus.html')

def myhomepage(request):
    return render(request,"Blood_Donation/home.html")