from django.urls import path
from .views import (index, top_sellers,
					advertisement_post, advertisement)

urlpatterns = [
	path('', index, name='index'),
	path('top-sellers/', top_sellers, name='top-sellers'),
	path('advertisement-post', advertisement_post, name='advertisement-post'),
	path('advertisement/<int:pk>', advertisement, name='advertisement')
]
