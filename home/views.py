from typing import Any
from django.views.generic import ListView
from .models import Car,CarBrand

# Create your views here.

class HomePage(ListView):
    model=Car
    template_name='home.html'
    context_object_name ='cars'

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['car_brands']=CarBrand.objects.all()
        return context


    
    
