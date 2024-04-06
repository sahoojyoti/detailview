from django.shortcuts import render, HttpResponse
from django.views.generic import *
from app.models import *
from django.urls import reverse_lazy

# Create your views here.

class InsertSchool(CreateView):
    model = School
    fields = '__all__'
    success_url = reverse_lazy('index')


def index(request):
    return HttpResponse('Insertion successfull')

def wish_someone(request, name):
    return HttpResponse(f"<h1> Hello {name} </h1>")

def obj(request, sname):
    obje = School.objects.get(sname=sname)
    d = {'obje':obje}  
    return render(request, 'app/obj.html', d) 

class School_list(ListView):
    model = School
    context_object_name = 'schools'
    

class School_detail(DetailView):
    model = School
    context_object_name = 'schools'
    
class updateschool(UpdateView):
    model=School
    fields='__all__'
    success_url='School_list'