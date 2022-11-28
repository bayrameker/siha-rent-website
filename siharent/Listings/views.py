from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Listings
from django.core.paginator import Paginator
from .choice import price_choices, country_choices, altitude_choices
# Create your views here.


def Index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def Listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/list.html', context)


def Search(request):

    queryset_list = Listings.objects.order_by('-list_date')

    # keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # company
    if 'company' in request.GET:
        company = request.GET['company']
        if company:
            queryset_list = queryset_list.filter(company__iexact=company)

            # company
            if 'country' in request.GET:
                company = request.GET['company']
                if company:
                    queryset_list = queryset_list.filter(country__iexact=company)

    
    # flight_time
    if 'flight_time' in request.GET:
        bedrooms = request.GET['flight_time']
        if bedrooms:
            queryset_list = queryset_list.filter(flight_time__lte=bedrooms)

    # took_off
    if 'took_off' in request.GET:
        price = request.GET['took_off']
        if price:
            queryset_list = queryset_list.filter(took_off__lte=price)



    context = {
        'country_choices': country_choices,
        'altitude_choices': altitude_choices,
        'price_choices': price_choices,
        'listings':queryset_list,
        'value':request.GET
    }
    return render(request, 'listings/search.html',context)
