"""
URL configuration for myproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from .views import reg_confirm
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('',views.demo),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('login/admin',views.login_admin,name='login_admin'),
    path('admin/about/',views.about_index,name='about'),    
    path('admin/reg/conf',views.reg_confirm,name='reg_conf'),
    path('admin/about/insert/',views.about_insert, name='about_insert'),
    path('admin/edit/<int:id>',views.edit_index,name='edit_index'),
    path('admin/edit/',views.about_edit,name='about_edit'),
    path('admin/delete/<int:id>',views.delete_index,name='delete_index'),
    path("admin/user/email_verification/<str:id>",views.email_verify,name='email_verify'),
]

