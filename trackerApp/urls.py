from django.urls import path

from .views import IndexView, RedirectView, LoginView, RegisterView, ProfileView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='redirect'),
    path('index/', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
]
