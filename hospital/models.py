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
    
class Composition(models.Model):
    """Active ingredient + strength, e.g. Paracetamol 500mg — shared by
    branded and generic medicines so matching is an exact ID join."""
    salt_name = models.CharField(max_length=200)   # e.g. "Paracetamol"
    strength = models.CharField(max_length=50)      # e.g. "500mg"

    class Meta:
        unique_together = ('salt_name', 'strength')

    def __str__(self):
        return f"{self.salt_name} {self.strength}"
    
class Medicine(models.Model):
    # --- keep your existing fields here, e.g.: ---
    image = models.ImageField(upload_to='hospital_images/', null=True, blank=True)    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    tablets = models.FloatField(default=0.0)
    Group_name = models.TextField(blank=True)
    # ... whatever else you already have ...

    # --- new fields for this feature ---
    composition = models.ForeignKey(Composition,on_delete=models.PROTECT,related_name='medicines',null=True)
    is_generic = models.BooleanField(default=False)

    def __str__(self):
        return self.name