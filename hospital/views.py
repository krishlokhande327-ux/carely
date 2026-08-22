from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views here.
def home(request):
    hospitals = Hospital.objects.all()
    if request.GET.get('search'):
        hospitals = hospitals.filter(name__icontains=request.GET.get('search'))
        
    profiles = profile.objects.all()
    return render(request,'home.html',{'hospitals':hospitals,'profiles':profiles})

def speciality_page(request):
    specialities = speciality.objects.all()
    if request.GET.get('search'):
        specialities = specialities.filter(speciality__icontains=request.GET.get('search'))
    return render(request, 'speciality.html', {'speciality': specialities})

def details(request,id):
    # hospitals = Hospital.objects.all()
    hospital_data = get_object_or_404(Hospital , id=id)
    return render(request,'hospital_details.html',{'hospital': hospital_data})

def medicines(request):
    return render(request, 'medicines.html')  
# def nearby_hospitals_page(request):
#     """Renders the map page (nearby_hospitals.html)."""
#     return render(request, "nearby_hospitals.html")

# def hospital_locations_api(request):
#     """
#     Returns hospital coordinates + basic info as JSON for Leaflet to consume.
#     Optional query params: ?specialty=cardiology&emergency=true
#     """
#     qs = Hospital.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
 
#     specialty = request.GET.get("specialty")
#     if specialty:
#         qs = qs.filter(specialty__icontains=specialty)
 
#     if request.GET.get("emergency") == "true":
#         qs = qs.filter(has_emergency=True)  # adjust field name to match your model
 
#     data = [
#         {
#             "id": h.id,
#             "name": h.name,
#             "specialty": getattr(h, "specialty", ""),
#             "rating": getattr(h, "rating", None),
#             "lat": float(h.latitude),
#             "lng": float(h.longitude),
#             "open_24x7": getattr(h, "open_24x7", False),
#         }
#         for h in qs
#     ]
#     return JsonResponse({"hospitals": data})