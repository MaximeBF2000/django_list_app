from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import List, Todo


# Create your views here.

def index(req):
    list_items = List.objects.all()
    todo_items = Todo.objects.all()
    return render(req, "index.html", {"lists": list_items, "todos": todo_items})


def add_list(req):
    new_list = List(name=req.POST["addlist"])
    new_list.save()
    return HttpResponseRedirect("/")


def delete_list(req, list_id):
    list_to_delete = List.objects.get(id=list_id)
    list_to_delete.delete()
    return HttpResponseRedirect("/")


def list_page(req, list_id):
  list_items = List.objects.all()
  todo_items = Todo.objects.filter(list_key=list_id)
  return render(req, "todo_list.html", {"lists": list_items, "todos": todo_items, "list_id": list_id})