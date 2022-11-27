from django.shortcuts import render
from Listings.models import Listings
from Sihas.models import Sihas
from Listings.choice import price_choices,altitude_choices,country_choices
# Create your views here.

def IndexPage(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'altitude_choices':altitude_choices,
        'country_choices':country_choices,
        'price_choices':price_choices
    }
    return render(request,'index.html',context)


def AboutPage(request):
    sihas = Sihas.objects.order_by('category')

    context = {
        'sihas':sihas,

    }
    return render(request,'about.html',context)