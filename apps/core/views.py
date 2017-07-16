from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Item


def index(request):
    return render(request, 'index.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/user-list/')
