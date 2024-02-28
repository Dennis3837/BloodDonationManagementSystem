from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.myhomepage,name='myhomepage'),
    path('donorhome/',views.donor_home,name='donorhome'),
    path('donorform/', views.donor_form, name='donorform'),
    path('donaredit<int:id>/', views.donor_form, name='donaredit'),
    path('donardelete<int:id>/', views.donor_delete, name='donardelete'),
    path('donorlist/', views.donor_list, name='donorlist'),
    
    path('customerform/', views.customer_form, name='customerform'),
    path('customeredit<int:id>/', views.customer_form, name='customeredit'),
    path('customerlist/', views.customer_list, name='customerlist'),
    path('customerdelete<int:id>/', views.customer_delete, name='customerdelete'),
    
    path('donorsuccess/', views.donor_success, name='donorsuccess'),
    path('customersuccess/', views.customer_success, name='customersuccess'),
    
    path('choice/',views.choice,name='choice'),
    path('contactus/',views.contactus,name='contactus'),


]
