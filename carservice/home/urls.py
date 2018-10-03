from . import views
from django.urls import path, include

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),


    path('carlist', views.carlist, name='carlist'),
    path('addcar', views.addcar, name='addcar'),
    path('editcar/<int:carid>', views.addcar, name='addcar'),
    path('updatecar', views.updatecar, name='updatecar'),
    path('delete/<int:carid>', views.deletecar, name='deletecar'),
    
]