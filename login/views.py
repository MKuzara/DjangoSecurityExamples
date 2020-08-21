from django.shortcuts import render
from .models import ExampleUser
from .forms import LoginForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                user = ExampleUser.objects.get(username=username)
                if user.compare_password(password):
                    return render(request, 'login/login.html', {'form': form, 'msg': 'Login successful'})
                return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid password'})
            except ExampleUser.DoesNotExist:
                return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid login'})
        else:
            return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid credentials'})
    return render(request, 'login/login.html', {'form': LoginForm()})

def login_v2(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                user = ExampleUser.objects.get(username=username)
                if user.compare_password(password):
                    return render(request, 'login/login.html', {'form': form, 'msg': 'Login successful'})
                return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid login or password'})
            except ExampleUser.DoesNotExist:
                return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid login or password'})
        else:
            return render(request, 'login/login.html', {'form': form, 'msg': 'Invalid credentials'})
    return render(request, 'login/login.html', {'form': LoginForm()})