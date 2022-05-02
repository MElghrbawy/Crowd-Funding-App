from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from django import forms
from django.forms.widgets import DateInput


class CustomRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username"
        )


# class CustomLogin(UserChangeForm):

#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = User
#         fields = ("email", )

class CustomLogin(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class Profile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "country",
            "mobile_phone",
            "date_of_birth",
            "avatar"
        )
        labels = {
            'date_of_birth': ('D.O.B'),
        }
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }
