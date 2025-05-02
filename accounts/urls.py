from django.urls import path
from allauth.account import views as account_views
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('login/',  account_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    
    
     
    
]
 