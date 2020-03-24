from django import forms


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

    your_genre = forms.ChoiceField(label='Género', choices=[('1','Masculino'),('2','Femenino')])

    your_position = forms.CharField(label='Cargo', max_length=20,
        widget=forms.TextInput(attrs={'class': 'expand'}))


    