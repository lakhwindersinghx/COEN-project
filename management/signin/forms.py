from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def __init__(self, *args, **kwargs):
        self.edit_mode = kwargs.pop('edit_mode', False)
        super(SignUpForm, self).__init__(*args, **kwargs)

        if self.edit_mode:
            # Exclude password fields in edit mode
            if 'password1' in self.fields:
                del self.fields['password1']
            if 'password2' in self.fields:
                del self.fields['password2']

    def save(self, commit=True):
        # Override save to handle when in edit mode
        if self.edit_mode:
            # Save without dealing with passwords
            user = super(UserCreationForm, self).save(commit=False)
            if commit:
                user.save()
            return user
        else:
            # Default save method, which includes password handling
            return super().save(commit=commit)


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ForgotPasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)