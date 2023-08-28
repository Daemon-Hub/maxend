from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


@login_required(login_url=reverse_lazy('login'))
def profile(request):
	context = {'main': 'profile'}
	return render(request, 'app_auth/profile.html', context)


def _login(request):
	context = {'main': 'login'}
	if request.method == 'GET':
		if request.user.is_authenticated:
			return redirect('profile')
		else:
			return render(request, 'app_auth/login.html', context)
	username = request.POST['username']
	password = request.POST['password']
	print(username, password)
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('profile')
	context['error'] = 'Пользователь не найден(('
	return render(request, 'app_auth/login.html', context)


def _logout(request):
	logout(request)
	return redirect('login')


# @login_required(login_url=reverse_lazy('profile'))
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()
			return redirect('index')
	else:
		form = RegisterForm()
	context = {'form': form, 'main': 'register'}
	return render(request, 'app_auth/register.html', context)
