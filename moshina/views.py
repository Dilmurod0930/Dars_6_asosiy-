from django.shortcuts import render, redirect,  get_object_or_404
from .models import Moshina

"""  model_name = models.CharField(max_length=100)  # Masalan: 'Gentra'
    model = models.CharField(max_length=100)  # Masalan: 'Chevrolet'
    color = models.CharField(max_length=50)  # Masalan: 'Qora'
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Masalan: 14500.00
    year = models.PositiveIntegerField()  # Masalan: 2023
    image = models.ImageField(upload_to='media/')  # Rasm uchun
    description = models.TextField(blank=True)  # Mashina haqida tavsif"""

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

def  moshina_update(request , id):
    moshina = Moshina.objects.get(id = id)
    if  request.method == 'POST':
        moshina.model_name  = request.POST.get('model_name')
        moshina.model = request.POST.get('model')
        moshina.color = request.POST.get('color')
        moshina.price = request.POST.get('price')
        moshina.year = request.POST.get('year')
        moshina.description = request.POST.get('description')
        image = request.FILES.get('image')
        if image:
            moshina.image = image
        moshina.save()
        return redirect('moshina_info', id = id)
    return render(request, 'moshina/moshina_update.html',  context={'moshina': moshina})



def  moshina_add(request , id):
    moshina = Moshina()
    if  request.method == 'POST':
        moshina.model_name = request.POST['model_name']
        moshina.model = request.POST['model']
        moshina.color = request.POST.get('color')
        moshina.price = request.POST.get('price')
        moshina.year = request.POST.get('year')
        moshina.description = request.POST.get('description')
        moshina.image = request.FILES.get('image')
        moshina.save()
        return redirect('moshina_lst')
    return render(request, "moshina/moshina_add.html", context={'moshina': moshina})
