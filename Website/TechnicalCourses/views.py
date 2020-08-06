from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Allcourses
# Create your views here.

def Courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('')
    return HttpResponse('<h1> This is my home page </h1>')

def detail(request,course_id):
    return HttpResponse('<h2> These are the course details for course id : '+str(course_id) +' </h2>')