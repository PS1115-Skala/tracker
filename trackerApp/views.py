from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Activity, User


class IndexView(generic.list.ListView):
    template_name = 'trackerApp/base_index.html'
    model = Activity
    context_object_name = 'my_activities'

class RedirectView(generic.base.RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class LoginView(generic.base.TemplateView):
    template_name = 'trackerApp/login.html'

class RegisterView(generic.base.TemplateView):
    template_name = 'trackerApp/register.html'


class ProfileView(generic.detail.DetailView):
    model = User
    template_name = "trackerApp/base_profile.html"
