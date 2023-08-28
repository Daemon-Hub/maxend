from django.urls import path
from .views import profile, _login, _logout, register

urlpatterns = [
	path('profile/', profile, name='profile'),
	path('login/', _login, name='login'),
	path('logout/', _logout, name='logout'),
	path('register/', register, name='register')
]

