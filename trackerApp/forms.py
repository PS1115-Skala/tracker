from django import forms
from django.db import models
from .models import *


class LoginForm(forms.Form):
    your_email = forms.EmailField(label='Correo Electrónico', max_length=100, 
        widget=forms.TextInput(attrs={'class': 'expand'}))
    your_pass = forms.CharField(label='Contraseña', max_length=16,
        widget=forms.TextInput(attrs={'class': 'expand', 'type': 'password'}))


class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Nombre', max_length=100, 
        widget=forms.TextInput(attrs={'class': 'expand'}))

    your_last_name = forms.CharField(label='Apellido', max_length=100,
        widget=forms.TextInput(attrs={'class': 'expand'}))

    your_email = forms.EmailField(label='Correo Electrónico', max_length=100,
        widget=forms.TextInput(attrs={'class': 'expand'}))

    your_pass = forms.CharField(label='Contraseña', max_length=16, min_length=5,
        widget=forms.TextInput(attrs={'class': 'expand', 'type': 'password'}))

    your_genre = forms.ChoiceField(label='Género', choices=[('M','Masculino'),('F','Femenino'), ('O', 'Otros')])

    your_position = forms.CharField(label='Cargo', max_length=20,
        widget=forms.TextInput(attrs={'class': 'expand'}))

class LoanRequestForm(forms.ModelForm):

    class Meta:
        model = LoanRequest
        exclude = ('id_user',)

    loan_amount = forms.DecimalField(label='Monto',
        widget=forms.TextInput(attrs={'class': 'expand'}))

    loan_message = forms.CharField(label="Justificación", max_length=200,  widget=forms.Textarea(attrs={'class': 'expand lolo'}))

    loan_date = forms.DateTimeField(label='Fecha de pago',
        widget=forms.SelectDateWidget())

class ActivityForm(forms.Form):
    your_title = forms.CharField(label='Titulo', max_length=80,
        widget=forms.TextInput(attrs=
            {
                'class': 'form-control text-center',
                'style': 'border: none;',
                'placeholder': 'Actividad',
                'type': 'text'
            }))
    # your_start = forms.DateTimeField(label='Inicio',
    #     widget=forms.TextInput(attrs=
    #         {
    #             'type': 'hidden'
    #         }))
    # your_start = forms.DateTimeField(widget=forms.SplitHiddenDateTimeWidget())
    your_start = forms.CharField(label='Inicio', max_length=80,
        widget=forms.TextInput(attrs=
            {
                'type': 'hidden'
            }))
