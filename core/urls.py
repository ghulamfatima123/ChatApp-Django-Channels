from django.urls import path
from . import views
#from room import views as room_views
from . import views as core_views
urlpatterns = [
    path('', views.frontpage, name="base"),
    #path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    #for login and logt we can also use auth_views.LoginView.as_view() by importing django.contrib.auth
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    #path('rooms/', room_views.room, name='room'), 
   # path('rooms/', core_views.room, name='room'),

    
]
