from django.shortcuts import render
from .models import Moshina

# Create your views here.
def main(request):
    return render(request, 'main.html')


def  moshina_lst(request):
    moshina = Moshina.objects.all()
    context = {'moshina': moshina}
    return render(request, 'moshina/moshina_lst.html', context = context)

def  moshina_info(request , id):
    moshina = Moshina.objects.get(id = id)
    context = {'moshina': moshina}
    return render(request, 'moshina/moshina_info.html', context = context)