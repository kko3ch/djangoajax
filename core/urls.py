from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save/', views.save_data, name='save')
]

