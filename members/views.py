from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Member

# Create your views here.
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  # Colonnes spécifiques de retour
  # Le values_list()Une méthode vous permet de revenir Seules les colonnes que vous spécifiez.
  # mydata = Member.objects.values_list('firstname')
  mydata = Member.objects.filter(firstname='Jane').values()
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  # context = {
  #   'fruits': ['Apple', 'Banana', 'Cherry', 'Ananas', 'Cocktail'],   
  # }
  context = {
    'mymembers': mymembers,
    'mydata': mydata,
    'x': True, 
  }
  return HttpResponse(template.render(context, request))

def demo(request):
  template = loader.get_template('index.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request)) 