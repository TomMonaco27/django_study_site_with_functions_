# Create your views here.
# Ctrl+D продублировать строку
# Ctrl+Y удалить текущую строку
# Ctrl+Alt+L - отформатировать все строки в файле под PEP8 (если о пичарме говорим)
# начинаем ввод и жмем Ctrl+Пробел -подсказки и автозавершение
# Ctrl+/ - быстро комментировать/разкомментировать строку/строки
# Ctrl+Q - документация по выбранному объекту
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Успешная регистрация аккаунта.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
        context = {
            'title': 'Страница регистрации',
            'form': form,
        }
        return render(request,'users/register.html',context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
               # return HttpResponseRedirect('/')
               # return HttpResponseRedirect(reverse('users:login'))
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Страница авторизации',
        'form': form,
    }
    return render(request,'users/login.html',context)


@login_required
def profile(request):
    user_req = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user_req)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile '))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user_req)

    context = {
            'title': 'Страница профайл',
            'form': form,
            'baskets': Basket.baskets,
            'total_quantity': Basket.total_quantity,
            'total_sum': Basket.total_sum,
        }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



