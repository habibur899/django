from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard')
]
