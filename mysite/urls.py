"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hospital.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='hospital-home'),
    path('speciality/', speciality_page , name="speciality"),
    path('hospital/<int:id>/',details,name='hospital_detail'),
    path('medicines/',medicines,name='medicines'),
    # path("nearby/", nearby_hospitals_page, name="nearby_hospitals"),
    # path("api/locations/", hospital_locations_api, name="hospital_locations_api"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()