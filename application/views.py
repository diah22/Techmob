from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def inscription(request):
    template=loader.get_template('application/index.html')
    return HttpResponse(template.render(request=request))