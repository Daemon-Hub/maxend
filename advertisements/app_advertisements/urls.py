from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('top-sellers/', top_sellers, name='top-sellers'),
	path('advertisement-post', advertisement_post, name='advertisement-post'),
	path('advertisement/', advertisement, name='advertisement'),
	path('login/', login, name='login'),
	path('profile/', profile, name='profile'),
	path('register/', register, name='register')
]
