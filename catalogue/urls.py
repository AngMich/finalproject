from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.catalogue_view, name='catalogue'),
    path('comics/<int:id>/', views.comic_detail_view, name='comic_detail'), 
    path('comics/<int:comic_id>/review/', views.add_review, name='add_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

]
