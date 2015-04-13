from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.template.loader import get_template
from django.template import Context


# Create your views here.

def todo(request):
    salida = ""
    lista = Pages.objects.all()
    salida += "Las paginas que hay son:" + "\n" + "<ul>"
    for fila in lista:
        salida += "<li>" + fila.name + "--" + str(fila.page) + "\n"
    salida += "</ul>"

    return HttpResponse(salida)


def handler(request, recurso):
    salida = ""

    if request.method == "PUT":
        if request.user.is_authenticated():
            fila = Pages(name=recurso, page=request.body)
            fila.save()
        else:
            salida += "No puedes crear una pagina sin estar registrado"
            return HttpResponse(salida)

    try:
        fila = Pages.objects.get(name=recurso)
        if request.user.is_authenticated():
            salida += "Estas registrado. Eres " + request.user.username + ""
            salida += " <br><a href='logout'>Logout</a><br><br>"
        else:
            salida += "No estas registrado -> "
            salida += "<a href='/admin/login/'>Autenticate</a><br><br>"
        salida += fila.page
        return HttpResponse(salida)
    except Pages.DoesNotExist:
        return HttpResponseNotFound('Pagina no encontrada: /%s.' % recurso)


def plantilla(request, recurso):

    salida = ""
    list = ""
    if recurso == "/":
        list = Pages.objects.all()

    else:
        if (len(recurso.split('/page/')) == 2):
            recurso = recurso.split('/page/')[1]
            list = Pages.objects.filter(name=recurso)
        else:
            recurso = recurso.split('/')[1]
            list = "Error: recurso no encontrado"

    template = get_template("index.html")
    c = Context({'lista': list,
                 'nombre': recurso,
                 'autor': "Cristina Rosell"})
    rend = template.render(c)
    return HttpResponse(rend)


def notfound(request, recurso):
    return HttpResponseNotFound("No tenemos " + recurso)
