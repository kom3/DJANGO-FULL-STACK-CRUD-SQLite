import json
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.decorators import csrf
from .models import Todo

# Create your views here.


@csrf.csrf_exempt
def create(request):
    data = request.POST
    Todo.objects.create(task=data.get('task'), owner=data.get(
        'owner'), status=data.get('status'))
    return HttpResponse("Created!")


@csrf.csrf_exempt
def read(request):
    todos_qres = Todo.objects.all()
    todos = json.loads(serialize('json', todos_qres))
    todos_dict = {'items': [item.get('fields') for item in todos]}
    return render(request, "index.html", todos_dict)


@csrf.csrf_exempt
def update(request):
    Todo.objects.filter(
        task=request.POST.get('task')).update(
        task=request.POST.get('new_task'),
        owner=request.POST.get('owner'),
        status=request.POST.get('status')
    )
    return HttpResponse("Update!")


@csrf.csrf_exempt
def delete(request):
    Todo.objects.filter(task=request.POST.get('task')).delete()
    return HttpResponse("Delete!")
