from . import views
from django.urls import path, include

app_name = 'adminstrator'

urlpatterns = [
   

    path('carlist/', views.carlist, name='carlist'),
    path('addcar/', views.addcar, name='addcar'),
    path('editcar/<int:carid>', views.addcar, name='addcar'),
    path('updatecar', views.updatecar, name='updatecar'),
    path('delete/<int:carid>', views.deletecar, name='deletecar'),
    
]