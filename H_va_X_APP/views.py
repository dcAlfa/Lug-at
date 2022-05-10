from django.shortcuts import render
from .models import *

def lugat(request):
    qidirish = request.GET.get('q')
    togri_var = Togri.objects.filter(soz=qidirish)
    if len(togri_var)==1:
        natogri_var = Natogri.objects.filter(togri=togri_var[0])
    else:
        n = Natogri.objects.filter(natogri_soz=qidirish)
        if len(n) == 1:
            togri_var = Togri.objects.filter(id=n[0].togri.id)
            natogri_var = Natogri.objects.filter(togri=togri_var[0])
        else:
            togri_var = "Kiritilgan so'z ma'lumotlar omborida yo'q"
            natogri_var = []

    data = {
        "togri":togri_var,
        "natogri":natogri_var
    }
    return render(request, "result.html", data)
