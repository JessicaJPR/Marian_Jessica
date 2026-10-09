from django.urls import path
from . import views

app_name = 'genero'

urlpatterns = [
    path('terror/', views.terror, name='terror'),
    path('crimen/', views.crimen, name='crimen'),
    path('comedia/', views.comedia, name='comedia'),
    path('romance/', views.romance, name='romance'),
    path('suspenso/', views.suspenso, name='suspenso'),
]