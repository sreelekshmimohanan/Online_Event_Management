from django.db import models


    
class Customer_Details(models.Model):
    name=models.CharField(max_length=150)
   
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    password=models.CharField(max_length=150)



class feedback_tbl(models.Model):
    user_id=models.CharField(max_length=150)
    feedback=models.CharField(max_length=150)
    
class booking_tbl(models.Model):
    event_id=models.CharField(max_length=150)
    user_id=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    status=models.CharField(max_length=150)   



class program_tbl(models.Model):
    event_name=models.CharField(max_length=150)
    venue=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    district=models.CharField(max_length=150)    
    description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='', blank=True, null=True)
                           

class event(models.Model):
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)


