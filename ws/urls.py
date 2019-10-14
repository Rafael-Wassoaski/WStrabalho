from django.urls import path
from django.conf.urls import include, url
from . import views



urlpatterns = [
    path('vistorias_all/', views.vistoria_list, name = 'vistorias_all'),
   # path('login/', views.LoginViewSet, name = 'LoginViewSet')
 

]