from django.shortcuts import render
from .models import Advertisement

def index(request):
	advertisements = Advertisement.objects.all()
	context = {
		'advertisements': advertisements,
	}
	return render(request, 'index.html', context)

def top_sellers(request):
	return render(request, 'top-sellers.html')

def advertisement_post(request):
	return render(request, 'advertisement-post.html')

def advertisement(request):
	return render(request, 'advertisement.html')

def login(request):
	return render(request, 'login.html')

def profile(request):
	return render(request, 'profile.html')

def register(request):
	return render(request, 'register.html')
