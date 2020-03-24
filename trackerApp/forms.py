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

    your_position = forms.CharField(label='Cargo', max_length=20,
        widget=forms.TextInput(attrs={'class': 'expand'}))


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