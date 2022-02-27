from django.http import HttpResponse
from django.shortcuts import render
from .models import student
# Create your views here.
def showdata(request):
    
    data=student.objects.all()
    stu={
        'data':data
    }
    return render(request,'update.html',stu)

def saveinquiery(request):
    if request.method=="POST":
        name=request.POST.get('name')
        element=request.POST.get('element')
        conselation= request.POST.get('conselation')
        havetodo=request.POST.get('havetodo')
        da=student(name=name,element=element,conselation=conselation,havetodo=havetodo)
        da.save()
    return render(request, 'index.html')