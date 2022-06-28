from django.shortcuts import render
from model.models.Aeropuerto import Aeropuerto
from accounts.models import Usuario
from django.contrib.auth import get_user

from model.models.Instalacion import Instalacion
def home(request):
    email=[]
    aeropuertos = Aeropuerto.objects.all()
    usuarios= Usuario.objects.all()
    user = get_user(request)
    instalaciones=[]
    if user.is_authenticated:
        id=user.id_role
        curretnt_inst=Instalacion.objects.filter(Id_A=id)
        for i in curretnt_inst:
            instalaciones.append(i.Id_A)
    for user in usuarios:
        email.append(user.email)
    return render(request, "gestion.html",{"aeropuertos": aeropuertos,"email":email,"instalaciones":instalaciones})
