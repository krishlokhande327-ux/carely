from django.db import models
# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default='Nagpur')
    about=models.TextField(default='This hospital provides quality healthcare services with experienced doctors, modern medical facilities and patient-focused care.')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    star = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='hospital_images/', null=True, blank=True)
    schemes = models.JSONField(default=list, blank=True)
    servise = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
class profile(models.Model):
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user
    
class speciality(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    schemes = models.TextField()
    star = models.FloatField(default=0.0)

    def __str__(self):
        return self.speciality