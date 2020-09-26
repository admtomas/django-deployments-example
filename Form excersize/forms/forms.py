from django import forms
from django.core import validators
from .models import User2s, UserProfileInfo
#code below is new
from django.contrib.auth.models import User



#*code below will check if name start with letter 'z'
def check_for_z(value):
    if value[0].upper() != 'z':
        raise forms.ValidationError("Name must start with capital 'z'")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label='Enter your email again:')
    #*BOT validation
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
#*code below show error that name
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 5:
            raise forms.ValidationError('Name is too short! Need 5 characters atleast.')
        return name
#*clean entire form
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

#*Form models excersize
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User2s
        #*to get all fields type code below
        fields = '__all__'

#* USER excersize...fields are coming from models.py
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_picture')