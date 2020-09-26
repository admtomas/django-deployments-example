"""mysite URL Configuration

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
from django.urls import path, include
from django.views.generic.base import TemplateView

#*...empty "" will load first matching ROUTE from apps URLS.PY
#*   for exampl firs path like home/ will create pathe home/index or home/form etc
urlpatterns = [
    path('', include('forms.urls')),
    path('templateurl/', include('forms.urls')),
    path('other/', include('forms.urls')),
    path('index/', include('forms.urls')),
    path('form/', include('forms.urls')),
    path('users/', include('forms.urls')),
    path('users2/', include('forms.urls')),
    path('user_page/', include('forms.urls')),
    path('special/', include('forms.urls')),
    path('logout/', include('forms.urls')),
    path('admin/', admin.site.urls),
    #!path below is for build in functions LOGIN & LOGOUT
    path('', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
