from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.conf import settings
from django.contrib import messages
# Create your views here.

from .forms import LoginForm, RegisterForm
from .models import Activity, UserData


class IndexView(LoginRequiredMixin, generic.list.ListView):
    login_url = '/login/'
    redirect_field_name = 'index'
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
                context = {'form': form}
                messages.info(request, 'Correo o contraseña inválido')
                return render(request, self.template_name, {'form': form})
        else:
            context = {'form': form}
            messages.info(request, 'Correo o contraseña inválido')
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form})


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
            genre = form.cleaned_data['your_genre']
            position = form.cleaned_data['your_position']
            try:
                user = User.objects.create_user(email, email, password)
                user.first_name = name
                user.last_name = last_name
                user.save()
                position = UserData(position=position, genre=genre, id_user=user)
                position.save()

                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/index/')
                else:
                    context = {'form': form}
                    messages.info(request, 'Error de Servidor')
                    return render(request, self.template_name, context)
            except:
                context = {'form': form}
                messages.info(request, 'Usuario Resgistrado')
                return render(request, self.template_name, context)
        context = {'form': form}
        messages.info(request, 'Datos inválidos')
        return render(request, self.template_name, {'form': form})


class ProfileView(generic.detail.DetailView):

    model = User
    template_name = "trackerApp/base_profile.html"

    def get(self, request, *args, **kwargs):
        userdata = UserData.objects.get(id_user=request.user)
        media_root = getattr(settings, 'MEDIA_ROOT', None)
        request.session['position'] = userdata.position
        request.session['description'] = userdata.description
        request.session['image'] = userdata.profileImage.url
        request.session['genre'] = userdata.genre
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        validator = EmailValidator()

        userdata = UserData.objects.get(id_user=request.user.id)
        request.session['position'] = userdata.position
        request.session['description'] = userdata.description
        email = request.POST['formInputEmail']
        inputPosition = request.POST['formInputPosition']
        inputDescription = request.POST['formInputDescription']
        inputGenre = request.POST['formInputGenre']
        inputImage = request.FILES.get('image')

        try:
            if(inputPosition != ""):  # Se introduce el cargo
                userdata.position = inputPosition
                userdata.save()

            if(inputGenre != ""):  # Se introduce el cargo
                userdata.genre = inputGenre
                userdata.save()
            if(inputImage != None and userdata.imageVerification()):

                userdata.eraseOldMedia()
                userdata.profileImage = inputImage
                userdata.save()

            if(inputDescription != ""):  # Se introduce la descripcion
                userdata.description = inputDescription
                userdata.save()

            validator(email)  # Se verifica que se haya introducido un email
            user = User.objects.get(id=request.user.id)
            user.username = email
            user.email = email
            user.save()

        except:
            return HttpResponseRedirect('/profile/')

        return HttpResponseRedirect('/profile/')


class ActivityView(generic.detail.DetailView):
    model = User
    template_name = "trackerApp/activity.html"


class LoanView(generic.detail.DetailView):
    model = User
    template_name = "trackerApp/base_loan.html"
