from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
	context = dict(aidv=Advertisement.objects.all())
	return render(request, 'app_advertisements/index.html', context)


def top_sellers(request):
	return render(request, 'app_advertisements/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
	if request.method == 'POST':
		form = AdvertisementForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = AdvertisementForm()

	return render(request, 'app_advertisements/advertisement-post.html', {'form': form})


def advertisement(request):
	return render(request, 'app_advertisements/advertisement.html')


