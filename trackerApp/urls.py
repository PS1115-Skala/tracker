from django.urls import path, include, re_path

from .views import IndexView, RedirectView, LoginView, RegisterView, ProfileView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='redirect'),
    re_path(r'^index/$', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]
