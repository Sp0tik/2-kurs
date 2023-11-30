from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models importUser
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailFields(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))

	first_name = forms.CharFields(label="", max_lenght=100, 
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))

	last_name = forms.CharFields(label="", max_lenght=100, 
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')