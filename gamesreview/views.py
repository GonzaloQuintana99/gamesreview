from django.http import HttpResponse
from django.template import Template, Context, loader

from random import randint

# from aplicacion.models import *

# def welcome(req):
#     return HttpResponse("Bienvenidos")

# def saludar(res, nombre):
#     response = f"Hola {nombre}"
#     return HttpResponse(response)

# def welcometemplate(req):
#     nombre = "Jose"
#     apellido = "Pepe"
#     curso = "ING"
#     notas = [8,2,3,5,10]
#     diccionario = {"nombre": nombre, "apellido": apellido, "curso": curso, "notas": notas}

#     plantilla = loader.get_template('welcome.html')
#     doc = plantilla.render(diccionario)
#     return HttpResponse(doc)

# def agregar_curso(req):
#     nro_comision = randint(1,200)
#     str_nombre = "Python"
#     curso = Curso(nombre=str_nombre, comision=nro_comision)
#     curso.save()
#     documento = f"Se acaba de crear un curso de {str_nombre}, comision {nro_comision}"
#     return HttpResponse(documento)