from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from .forms import SignUpForm, SignInForm, ForgotPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.models import User
from django.conf import settings

# ------------------------------------------------------
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in after signing up
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired URL name for the home page

    else:
        form = SignUpForm()
    return render(request, 'signin/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with your desired URL name for the home page
    else:
        form = SignInForm()
    return render(request, 'signin/signin.html', {'form': form})


@login_required(login_url='signin')
def Logout(request):
    logout(request)
    return redirect('index')

def forgotpassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    form.save(
                        request=request,
                        use_https=request.is_secure(),
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        email_template_name='registration/password_reset_email.html'
                    )
                # Redirect to a new URL:
                return redirect('password_reset_done')
            else:
                form.add_error(None, "No user is associated with this email address")
    else:
        form = PasswordResetForm()
    return render(request, 'signin/forgotpassword.html', {'form': form})
