from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Advertisement, User
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def index(request):
	search = request.GET.get('query')
	if search:
		adv = Advertisement.objects.filter(title__contains=search)
	else:
		adv = Advertisement.objects.all()
	context = {'adv': adv, 'main': 'index', 'search': search}
	return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
	users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
	context = {'main': 'top', "users": users}
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


def advertisement(request, pk):
	adv = Advertisement.objects.get(id=pk)
	context = {"adv": adv, "main": "adv"}
	return render(request, 'app_advertisements/advertisement.html', context)
