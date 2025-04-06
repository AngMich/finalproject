from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.catalogue_view, name='catalogue'),
    path('comics/<int:id>/', views.comic_detail_view, name='comic_detail'), 
]
