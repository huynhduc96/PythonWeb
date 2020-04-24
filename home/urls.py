from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import RegisterView

urlpatterns = [
    path('', views.index, name = "home"),
    path('book/<int:id>/', views.book_detail, name = "book_detail"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
