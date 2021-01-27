from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request) :
    template = loader.get_template('exercise1.html')
    context = {'result':'정하늘'}
    return HttpResponse(template.render(context, request))

def exercise2(request):
    if request.method == 'POST':
        name = str(request.POST['name'])
        opinion = str(request.POST['opinion'])
        context = { 'name': name    , 'opinion': opinion}
    else :
         context = None
    return render(request, 'exercise2.html', context)