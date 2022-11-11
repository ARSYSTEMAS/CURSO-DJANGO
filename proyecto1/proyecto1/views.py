from django.http import HttpResponse
import datetime
from django.template import Template , Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self,nombre,apellido,edad,direccion):
        self.nombre     = nombre
        self.apellido   = apellido
        self.edad       = edad
        self.direccion  = direccion




def index(request):

    documento = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">',
                '<html xmlns="http://www.w3.org/1999/xhtml">',
                '<head>',
                '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />',
                '<title>MI PRIMERA PAGINA WEB DJANGO</title></head>',
                '<body>',
                '<p><strong>Hola esta es mi primera pagina web con django</strong></p>',
                '<p><strong>BIENVENIDOS</strong></p>',
                '</body>',
                 '</html>')

    return HttpResponse(documento)


def saludo(request):


    Datos = Persona("CAMILA","LEAL",34,"GUACARA")

    temas = ['administracion','matematicas','ingles','idiomas','php']

    #variables
    nombre = 'anderson'
    apellido = 'garcia'
    fecha    = datetime.datetime.now()

   #-------------------------------------------------------------------------------------------------------------------#
   # doc_externo = open("D:\PROYECTOS DJANGO\proyecto1\proyecto1\Templates\miPlantilla.html")

    #creamos objeto tipo template

    # plt = Template(doc_externo.read())

    #cerramos el doc_externo

    # doc_externo.close()

    #creamos contexto

    # ctx = Context({"nombre_persona":Datos.nombre,"apellido_persona":Datos.apellido,"fecha":fecha,"temas":temas})

    #renderizamos

    # documento = ctx.render(ctx)
    # -----------------------------------------------------------------------------------------------------------------#



    ####### Cargar templates con Settings #######

    # TEMPLATES = get_template('miPlantilla.html')

    # DOCUMENTO_TEMPLATES = TEMPLATES.render({"nombre_persona":Datos.nombre,"apellido_persona":Datos.apellido,"fecha":fecha,"temas":temas})

    # return HttpResponse(DOCUMENTO_TEMPLATES)

    ####### Cargar templates con Shortcut Render #######

    return render(request,"miPlantilla.html",{"nombre_persona":Datos.nombre,"apellido_persona":Datos.apellido,"fecha":fecha,"temas":temas})


def damefecha(request):
    fecha = datetime.datetime.now()
    documento = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
                <title>MI PRIMERA PAGINA WEB DJANGO</title></head>
                <body>
                <p><strong>Hola esta es la fecha actual: %s </strong></p>
                <p><strong>BIENVENIDOS</strong></p>
                '</body>
                </html>''' %fecha

    return HttpResponse(documento)


def calculaedad(request , ano):

    edadactual = 38
    periodo = ano - 2022

    edadfutura = edadactual+periodo

    documento ='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
                <title>MI PRIMERA PAGINA WEB DJANGO</title></head>
                <body>
                <p><strong>En el año: %s tendras %s años</strong></p>
                <p><strong>BIENVENIDOS</strong></p>
                '</body>
                </html>''' %(ano,edadfutura)

    return HttpResponse(documento)


def calculaedadparametros(request , edad, agno):

    periodo = agno - 2022

    edadfutura = edad+periodo

    documento ='''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
                <title>MI PRIMERA PAGINA WEB DJANGO</title></head>
                <body>
                <p><strong>En el año: %s tendras %s años</strong></p>
                <p><strong>BIENVENIDOS</strong></p>
                '</body>
                </html>''' %(agno,edadfutura)

    return HttpResponse(documento)




def cursoC(request):
    fecha = datetime.datetime.now()

    return render(request,"CursoC.html", {"fecha":fecha})

def cursoCss(request):

    return render(request,"Cursocss.html")



