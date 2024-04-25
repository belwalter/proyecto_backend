from django.shortcuts import render
from funko_api.models import Funko
from django.http import JsonResponse

# Create your views here.




def get_all_funkos():
    return Funko.objects.all().order_by('number')

def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)

