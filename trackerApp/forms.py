from django import forms

class LoginForm(forms.Form):
    your_email = forms.EmailField(label='Correo Electrónico', max_length=100)
    your_pass = forms.CharField(label='Contraseña', max_length=16)

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Nombre', max_length=100)
    your_last_name = forms.CharField(label='Apellido', max_length=100)
    your_email = forms.EmailField(label='Correo Electrónico', max_length=100)
    your_pass = forms.CharField(label='Contraseña', max_length=16)
    your_position = forms.CharField(label='Cargo', max_length=20)