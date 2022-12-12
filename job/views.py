from django.shortcuts import render
from .models import Employer
from django.http import HttpResponse


def choose(request):
    return render(request, 'choose.html')


def form(request):

    if request.method == "GET" :
        return render(request, 'form.html')

    elif request.method == "POST" :
        nam = request.POST["emp_name"]
        sherkat= request.POST["company"]
        adres= request.POST["adress"]
        codeposti= request.POST["code_posti"]
        tarikh= request.POST["comp_date"]
        sh_telephone= request.POST["phone_number"]
        shoghl= request.POST["need_job"]
        jensiat= request.POST["gender"]
        Employer.objects.create(name= nam, company= sherkat, adress= adres, code_posti= codeposti, date= tarikh, ph_number= sh_telephone, job= shoghl, gender= jensiat)

        return HttpResponse("saved successfully")

def result(request):

    a = {"data": Employer.objects.all()}

    return render(request, 'result.html', context=a)


