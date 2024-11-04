# from django import forms
# from django.contrib.auth.models import User
# from .models import Package
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# import datetime
# class PackageForm(forms.ModelForm):
#     class Meta:
#         model = Package
#         fields = '__all__'
#         # fields = ['source', 'destination','seats','room']
#
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#     def clean(self):
#         cleaned_data = super(UserCreationForm, self).clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")
#
#         if password1 != password2:
#             raise forms.ValidationError(
#                 "password and confirm_password does not match"
#             )
# class SignInForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         # widgets ={
#         #     'username': forms.TextInput(attrs={'class': "form-control"}),
#         #     'password': forms.PasswordInput(attrs={'class': "form-control"}),
#         # }
#
#
# class SearchForm(forms.Form):
#     search_query = forms.CharField(max_length=100)
#
# class ForgotPasswordForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)