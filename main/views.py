from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import House
from django.views import generic
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    try:
        house_list = House.objects.all()
    except House.DoesNotExist:
        raise Http404("House doesn't exist")
    context = {
        'house_list': house_list
    }
    return render(request, 'main/index.html', context)

def house(reuqest, house_id):
    house = get_object_or_404(House, pk=house_id)
    return HttpResponse("This is the detail page for house: [%s (%s)]" % (house.name, house.id))

def loading(request):
    return render(request, 'main/loading.html', {})

def home(request):
    return render(request, 'main/home.html', {})
# debug session start
def dbg(request):
    return render(request, 'main/house_detail.html', {})
# debug session end

class IndexView(generic.ListView):
    model = House
    template_name = 'main/index.html' # default is main/house_list.html
    # by default, context_object_name = 'house_list', the variable(model list) used in template

class DetailView(generic.DetailView):
    # by default, template_name = 'main/house_detail.html'
    model = House


