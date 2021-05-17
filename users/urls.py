from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import RegisterUser

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('user:login')), name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]