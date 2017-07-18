from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
	return render(request, 'home/index.html', {'context': "context"})

def about(request):
	return render(request, 'home/about.html', {'context': "context"})