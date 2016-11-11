from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Person

def index(request, context):
    ctx = {'ctx_templates':context}
    print(context)
    return render(request, 'polls/index.html', ctx)

def person_list(request):
    persons = Person.objects.all()
    ctx = {'persons': persons}
    return render(request, 'polls/list.html', ctx)

def person_add(request):
    if request.POST:
        person = Person(name=request.POST.get('person_name'))
        person.save()
        return HttpResponseRedirect(reverse('list'))
    return render(request, 'polls/form.html')

