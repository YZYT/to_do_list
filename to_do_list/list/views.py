from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
# Create your views here.


def home(request):
    to_do_items = models.ToDoList.objects.all().order_by('-created')

    return render(request, 'base.html', {'to_do_items': to_do_items})


def add_to_do(request):
    # print(request.POST['content'])
    content = request.POST.get('content')
    if content:
        models.ToDoList.objects.create(content=content)

    return HttpResponseRedirect('/')


def del_to_do(request, to_do_item_id):
    models.ToDoList.objects.get(id=to_do_item_id).delete()
    return HttpResponseRedirect('/')
