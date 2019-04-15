from django.shortcuts import render
from django .template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms

def index(request):
	context = {}
	return render(request, 'index.html',context)

def logout(request):
	if request.method == "POST":
		logout(request)
		return HttpResponse(Redirect(reverse('login')))

def chat(request):
	if request.method == "POST":
		logout(request)
		return HttpResponse(Redirect(reverse('index')))