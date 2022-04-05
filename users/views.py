from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
	
	return render(request, 'tranog/register.html', {})
