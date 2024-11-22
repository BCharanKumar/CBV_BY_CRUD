from django.shortcuts import render

# Create your views here.
from appp.models import *
from django.views.generic import *
class SchoolList(ListView):
    model=School
    #queryset=School.objects.all()
    context_object_name='schools'
    #template_name='school_ist.html'


