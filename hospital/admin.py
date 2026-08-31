from django.contrib import admin
from .models import Hospital,profile, speciality,Composition,Medicine
# Register your models here.
admin.site.register(Hospital)
admin.site.register(profile)
admin.site.register(speciality)
admin.site.register(Medicine)
admin.site.register(Composition)