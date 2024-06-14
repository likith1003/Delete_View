from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def School_list_fbv(request):
    schools = School.objects.all()
    d = {'schools': schools}
    return render(request, 'School_list_fbv.html', d)


class School_list(ListView):
    model = School
    context_object_name = 'schools'
    ordering = ['sname']


class displayschool(DetailView):
    model=School
    context_object_name='schoolobj'


class insert_school(CreateView):
    model=School
    fields='__all__'
    success_url="School_list"


class updateschool(UpdateView):
    model = School
    fields='__all__'
    success_url='School_list'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobj'
    success_url='School_list'