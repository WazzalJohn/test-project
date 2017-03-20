from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
#
    # #Botcatcher manual validation example.
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha BOT!')
    #     return botcatcher

class Settings(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class SignIn(forms.ModelForm):
    # specifying fields specifically for the form (matching the model)
    # don't have to do this.
    # firstname = forms.CharField()
    # lastname = forms.CharField()
    # email = forms.EmailField()
    # password = forms.CharField()

    class Meta():
        model = User
        #fields = "__all__"      # everything
        fields = ("email", "password")      # specific fields only
        # exclude = ["field1", "field2"]      #all fields except for these ones.
