# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_view, name='room'),
    path('<slug:slug>/', views.oneroom, name='oneroom'),
    #the first slug is type parameter and the second is name which is in view 
]
