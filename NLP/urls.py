from django.urls import path

from . import views, text2info

app_name = 'NLP'
urlpatterns = [
    path('', views.home, name='home'),
    path('maps/',views.maps,name='maps'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('test/',views.index,name='index'),
]