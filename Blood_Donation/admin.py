from django.contrib import admin
from.models import Blood_Group,District,Donor,Request_Customer
# Register your models here.

admin.site.register(Request_Customer)
admin.site.register(Blood_Group)
admin.site.register(District)
admin.site.register(Donor)
