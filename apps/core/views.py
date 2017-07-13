from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Item


def index(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    return render(request, 'index.html')
