from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm


def index(request):
	context= dict(aidv=Advertisement.objects.all())
	return render(request, 'index.html', context)


def top_sellers(request):
	return render(request, 'top-sellers.html')


def advertisement_post(request):
	if request.method == 'POST':
		form = AdvertisementForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = AdvertisementForm()
	context={'form': form}
	return render(request, 'advertisement-post.html', context)


def advertisement(request):
	return render(request, 'advertisement.html')


def login(request):
	return render(request, 'login.html')


def profile(request):
	return render(request, 'profile.html')


def register(request):
	return render(request, 'register.html')
