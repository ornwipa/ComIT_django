from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django.http import response
from django.template.response import SimpleTemplateResponse
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from first_app.views import hello_world
from people.models import Person

def display_person_info(request, pk):
    person = Person.objects.get(pk=pk)
    data_context = {
        'person': person
    }
    return SimpleTemplateResponse('person.html', data_context)

class PersonInfo(View):

    def get(request, *args, **kwargs):
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        data_context = {
            'person': person
        }
        return SimpleTemplateResponse('person.html', data_context)

    def post(request, *args, **kwargs):
        data_context = {}
        return SimpleTemplateResponse('person.html', data_context)

class PersonInfo(TemplateView):

    template_name = 'person.html' # allow to define template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # inherite from TemplateView
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person
        return context # return only context to render in template

class PersonInfoMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person 
        return context
    
class PersonInfo(PersonInfoMixin, TemplateView):

    template_name = 'person_html'

class DrawOnProfilePic(PersonInfoMixin, TemplateView):    
    pass

class PersonListView(ListView):

    template_name = 'person_list.html'
    model = Person
    