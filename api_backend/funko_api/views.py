from django.http import JsonResponse
from django.shortcuts import render

from funko_api.models import Funko
from funko_api.serializers import FunkoSerializer
# Create your views here.


def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data

def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)


def users_rest(request):
    # funkos = get_all_funkos()
    return JsonResponse("Ok", safe=False)
