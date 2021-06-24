from django.urls import path

from admins.views import index, admin_user, admin_users_create, admin_users_update, admin_users_no_active, admin_users_active,\
    admin_users_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_user, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:id>', admin_users_update, name='admin_users_update'),
    path('users/no_active/<int:id>', admin_users_no_active, name='admin_users_no_active'),
    path('users/active/<int:id>', admin_users_active, name='admin_users_active'),
    path('users/delete/<int:id>', admin_users_delete, name='admin_users_delete'),
]