from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    data = stud_record.objects.all() 
    form = stud_record_form()
    if request.method == 'POST':
        form = stud_record_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'students/home.html',{'data':data, 'form':form})

def update(request,id):
    upda = stud_record.objects.get(id=id)
    task = stud_record_form(instance=upda)

    if request.method =='POST':
        form = stud_record_form(request.POST, instance= upda)
        if form.is_valid():
            form.save()
        return redirect("/")

    return render(request, 'students/updatedata.html', {'task':task})

def delete(request,pk):
    dele = stud_record.objects.get(id=pk)
    
    if request.method == 'POST':
        dele.delete()
        return redirect("/")

    return render(request,'students/deletedata.html',{'dele':dele})