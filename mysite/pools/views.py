from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    latest_question = Question.objects.order_by('-pub_date')
    context = {'latest_question':latest_question}
    return render(request,'pools/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    #context = {'question':question}
    return render(request,'pools/details.html',{'question':question})

def results(request, question_id):
    return HttpResponse('result of question %s'  %question_id)

def vote(request, question_id):
    return HttpResponse('vote of question %s'  %question_id)


