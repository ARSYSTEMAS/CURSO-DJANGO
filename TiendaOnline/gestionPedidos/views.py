from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import forms_contact
# Create your views here.


def search_productos(request):

    return render(request,"searchproductos.html")


def buscar(request) -> dict:



    codigo: int   = request.GET["cod"]
    articulo: str = request.GET["prd"]


    if  articulo:
        #mensaje = f'El articulo encontrado es: {articulo}, con el codigo de barra {codigo}'
        if len(articulo) > 20:

            mensaje = 'ERROR. Texto de busqueda Demasiado largo'

        else:
            articulos = Articulos.objects.filter(nombre__icontains=articulo)

            return render(request, "productos.html", {"art": articulos, "query": articulo})

    else:
        mensaje = 'ERROR. Debes introducir un producto a buscar'

    return HttpResponse(mensaje)

@csrf_exempt 
def form_contacto(request):


    if request.method=='POST':

        SUBJECT = request.POST["txt_asunto"]

        MESSAGE = request.POST["txt_message"] + " " + request.POST["txt_email"]

        EMAIL_FROM    = settings.EMAIL_HOST_USER

        RECIPIENT_LIST = ["abi.leal1990@gmail.com"]

        send_mail(SUBJECT,MESSAGE,EMAIL_FROM,RECIPIENT_LIST,fail_silently=False)

        return render(request,"gracias.html")

    return render(request,"contacto.html")


@csrf_exempt 
def form_contacto_new(request):

    if request.method=='POST':

        formulario = forms_contact(request.POST)

        if formulario.is_valid():

            infForm=formulario.cleaned_data

            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email',''),['abi.leal1990@gmail.com'],)

            return render(request,"gracias.html")
    else:

        formulario = forms_contact()

    return render(request,"form_contacto.html",{'form':formulario})

