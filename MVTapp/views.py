from ssl import HAS_TLSv1_1
from django.http import HttpResponse
from django.shortcuts import render

from MVTapp.models import familia

# Create your views here.


def mi_vista(request):
     return HttpResponse('<h1>Hola,conoce a mi Familia</h1>')
 
 
def nueva_vista(request):
    
    # familia1=familia(nombre='maria',edad='50',fecha_de_nacimiento='1975-10-13')
    # familia2=familia(nombre='jose',edad='60',fecha_de_nacimiento='1978-9-4')
    # familia3=familia(nombre='sol',edad='30',fecha_de_nacimiento='1992-7-8')
    
    # familia1.save()
    # familia2.save()
    # familia3.save()
    
    lista_familia1 = familia.objects.all()
    
    return render(request,'index.html',{'lista_de_objetos':[familia1,familia2,familia3]})