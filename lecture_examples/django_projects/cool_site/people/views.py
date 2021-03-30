from django.shortcuts import render, redirect, HttpResponse
from django.http import response
from django.template.response import SimpleTemplateResponse
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView
from people.models import Person
from people.forms import FirstNameForm

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
        context = super().get_context_data(**kwargs) # inherited from TemplateView
        pk = kwargs.get('pk')
        person = Person.objects.get(pk=pk)
        context['person'] = person

        if self.request.method == 'POST':
            context['form'] = FirstNameForm(self.request.POST) # add form to data context
        else:
            context['form'] = FirstNameForm()

        return context # return only context to render in template

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        person = context['person']
        # first_name = request.POST['first_name']
        # person.first_name = first_name
        # person.save()
        # return redirect('people-list')

        form = context['form']
        # form = FirstNameForm(data=request.POST) # POST contains data submitted to the form
        if form.is_valid():
            person.first_name = form.cleaned_data['first_name'] # match name in form to model
            person.save()
            return redirect('people-list')
        else:
            return render(request, self.template_name, context=context)

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
    