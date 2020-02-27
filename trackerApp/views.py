from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

from .forms import LoginForm, RegisterForm
from .models import Activity, UserPosition


class IndexView(generic.list.ListView):
    template_name = 'trackerApp/base_index.html'
    model = Activity
    context_object_name = 'my_activities'

class RedirectView(generic.base.RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

class LoginView(generic.edit.FormView):
    form_class = LoginForm
    template_name = 'trackerApp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['your_email']
            password = form.cleaned_data['your_pass']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return render(request, template_name, {'form':form})
        
        return render(request, template_name, {'form':form})

    

class RegisterView(generic.base.TemplateView):
    form_class = RegisterForm
    template_name = 'trackerApp/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            last_name = form.cleaned_data['your_last_name']
            email = form.cleaned_data['your_email']
            password = form.cleaned_data['your_pass']
            position = form.cleaned_data['your_position']

            user = User.objects.create_user(email, email, password)
            user.first_name = name
            user.last_name = last_name
            user.save()
            position = UserPosition(position=position, id_user=user)
            position.save()
            return HttpResponseRedirect('/index/')
        
        return render(request, template_name, {'form':form})


class ProfileView(generic.detail.DetailView):
    model = User
    template_name = "trackerApp/base_profile.html"
