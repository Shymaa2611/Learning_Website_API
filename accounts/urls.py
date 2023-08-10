from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI,ProfileView,contactView
from . import views
from django.urls import path



urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/profile/',ProfileView.as_view(), name='profile'),
    path('api/contact/',contactView.as_view(), name='profile'),

    #path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
   
     

]