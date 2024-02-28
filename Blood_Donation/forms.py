from django import forms
from .models import Donor, Request_Customer

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # Add more widgets for other fields if needed
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Request_Customer
        fields = "__all__"
        # You can add widgets here for specific fields if needed
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # Add more widgets for other fields if needed
        }
        
