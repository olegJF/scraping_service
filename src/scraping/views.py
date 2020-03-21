from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    # print(request.GET)
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if language:
            _filter['language__name'] = language

        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs})
