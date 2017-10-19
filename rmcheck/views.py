from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rmcheck.forms import SignUpForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

from .models import Ramyeon


def index(request) :
	return render(request, 'rmcheck/index.html')

def about(request) :
	return render(request, 'rmcheck/about.html')

def grammar(request) :
	ramyeons = Ramyeon.objects.all()
	context = {'ramyeons' : ramyeons}

	if request.user.is_authenticated():
		return render(request, 'rmcheck/grammar.html', context)
	else:
		messages.warning(request, '로그인하신 후 사용하실 수 있습니다.') 
		return render(request, 'rmcheck/index.html')

def signup(request) :
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect(index)
	else:
		form = SignUpForm()
	return render(request, 'rmcheck/signup.html', {'form':form})