# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# CRUD

# READ
@user_passes_test(lambda u: u.is_superuser)
def admin_user(request):
    context = {'title': 'Админ | Пользователи', 'users': User.objects.all()}
    messages.success(request, 'Поздравляем! Успешное создание аккаунта (def admin_user).')
    return render(request, 'admins/admin-users-read.html', context)

# CREATE
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Успешное создание аккаунта (def admin_users_create).')
            #return render(request, 'admins:admin_user_create')
            return HttpResponseRedirect(reverse('admins:admin_user'))
    else:
        form = UserAdminRegisterForm()
    context = {
            'title': 'Админ | Страница создания аккаунта',
            'form': form,
        }
    return render(request, 'admins/admin-users-create.html', context)

# UPDATE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Админ | Обновление пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html',context)

# Mark is NO active
@user_passes_test(lambda u: u.is_superuser)
def admin_users_no_active(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

# Mark is YES active
@user_passes_test(lambda u: u.is_superuser)
def admin_users_active(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))

# DELETE
@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))