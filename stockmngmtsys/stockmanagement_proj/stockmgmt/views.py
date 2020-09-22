from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm

def home(request):
	title = 'Homepage'
	form = 'welcome: This is the home page'
	context = {
		"title": title,
		"test": form,
	}
	return render(request, 'home.html', context)
# Create your views here.

def list_items(request):
	title = 'List of list_items'
	queryset = Stock.objects.all()
	context= {
		"title": title,
		"queryset" : queryset
	}
	return render(request, 'list_items.html', context)

def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_items')
	context = {
		"form":form,
		"title" : "Add Item",
	}
	return render(request, "add_items.html", context)