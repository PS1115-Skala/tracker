from django import forms

class LoginForm(forms.Form):
    your_email = forms.EmailField(label='Email', max_length=100)
    your_pass = forms.CharField(label='Password', max_length=16)

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='FirstName', max_length=100)
    your_last_name = forms.CharField(label='lastName', max_length=100)
    your_email = forms.EmailField(label='Email', max_length=100)
    your_pass = forms.CharField(label='Password', max_length=16)
    your_position = forms.CharField(label='Position', max_length=20)