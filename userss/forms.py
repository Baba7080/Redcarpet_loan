from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import loan
#Login Form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
        {'autocomplete':'current-password', 'class':'form-control'}))

class applyloan(forms.ModelForm):
    class Meta:
        model = loan
        fields = ['user','Amount',]
    def save(self, user=None):
        user_profile = super(applyloan, self).save(commit=False)
        if user:
            user_profile.user = user
            print(user)
        user_profile.save()
        return user_profile


class loanStatus(forms.ModelForm):
    class Meta:
        model = loan
        fields = ['user','Approved']




    # hello@cowhite.com