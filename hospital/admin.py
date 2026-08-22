from django.contrib import admin
from .models import Hospital,profile, speciality
# Register your models here.
admin.site.register(Hospital)
admin.site.register(profile)
admin.site.register(speciality)