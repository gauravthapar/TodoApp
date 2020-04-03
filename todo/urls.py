"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signupuser, name = 'signupuser'),
    path('login/',views.loginuser, name ="loginuser"),
    path('logout/',views.logoutuser, name = 'logoutuser'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(template_name = 'todolist/password_reset.html'), 
        name = "password_reset"
    ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name = 'todolist/password_reset_sent.html'), 
        name = "password_reset_done"
    ),
    path('password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'todolist/password_reset_form.html'), 
        name = "password_reset_confirm"
    ),
    path('password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'todolist/password_reset_done.html'), 
        name = "password_reset_complete"
    ),



    path('',views.home, name = "home"),
    path('current/',views.currenttodods, name = "currenttodos"),
    path('completed/',views.completedtodos, name = "completedtodos"),
    path('create/',views.createtodo, name = "createtodo"),
    path('todo/<int:todo_pk>', views.viewtodo, name = "viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name = "completetodo"),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name = "deletetodo"),
]




#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']