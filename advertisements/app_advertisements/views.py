from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def index(request):
	title = request.GET.get('query')
	if title:
		aidv = Advertisement.objects.filter(title=title)
	else:
		aidv = Advertisement.objects.all()
	context = {'aidv': aidv, 'main': 'index'}
	return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
	context = {'main': 'top'}
	return render(request, 'app_advertisements/top-sellers.html', context)


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
	if request.method == 'POST':
		form = AdvertisementForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = AdvertisementForm()
	context = {'main': 'adv_post', 'form': form}
	return render(request, 'app_advertisements/advertisement-post.html', context)


def advertisement(request):
	context = {'main': 'adv'}
	return render(request, 'app_advertisements/advertisement.html', context)


