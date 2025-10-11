from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hire/', views.hire, name='hire'),
    path('projects/', views.projects, name='projects'),
    path('testimonial/', views.testimonial, name='testimonial'),

]
