from django.db import models

# Create your models here.

# model for Blood-Group
class Blood_Group(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

# model for District
class District(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# model for Donor
class Donor(models.Model):
    
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]    
    
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    blood_group = models.ForeignKey(Blood_Group,on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    # model for request_customer
class Request_Customer(models.Model):
    
    GENDER_CHOICES = [
      ('Male','Male'),
      ('Female','Female'),
      ('Other','Other'),
    ] 
        
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    blood_group = models.ForeignKey(Blood_Group,on_delete=models.CASCADE)
    email = models.EmailField()