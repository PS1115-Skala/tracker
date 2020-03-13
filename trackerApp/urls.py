from django.urls import path, include, re_path

from .views import IndexView, RedirectView, LoginView, RegisterView, ProfileView, LoanView

app_name = 'trackerApp'
urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='redirect'),
    re_path(r'^index/$', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('loan/<int:pk>/', LoanView.as_view(), name='loan'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]
