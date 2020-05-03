from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .forms import FindForm
from .models import Vacancy


def home_view(request):
    # print(request.GET)
    form = FindForm()

    return render(request, 'scraping/home.html', {'form': form})


def list_view(request):
    # print(request.GET)
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    context = {'city': city, 'language': language, 'form': form}
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        qs = Vacancy.objects.filter(**_filter)
        paginator = Paginator(qs, 10)  # Show 10 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
    return render(request, 'scraping/list.html', context)


def v_detail(request, pk=None):
    # object_ = Vacancy.objects.get(pk=pk)
    object_ = get_object_or_404(Vacancy, pk=pk)
    return render(request, 'scraping/detail.html', {'object': object_})


class VDetail(DetailView):
    queryset = Vacancy.objects.all()
    template_name = 'scraping/detail.html'
    # context_object_name = 'object'
