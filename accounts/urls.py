from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/confirm/', auth_views.LogoutView.as_view(next_page='catalogue:catalogue'), name='logout'),
    path('accounts/logout/', views.logout_user, name='logout_user'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/employee/', views.employee_panel, name='employee'),
    path('accounts/employee/edit/<int:comic_id>/', views.employee_panel, name='edit_comic'),
]
