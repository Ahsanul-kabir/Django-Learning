"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),   # code for video : 4
    path('',views.index_func,name='index'),   # code for video : 4
    path('about/',views.about_func,name='about'),  # code for video : 4
    path('html/',views.html_func,name='html'),  # code for video : 5
    path('text/',views.read_file_func,name='txt'),  # code for video : 5
    path('navigator/',views.navigator_func,name='navigator'),  # code for video : 6


    path('removepunc', views.removepunc, name='rempun'),    # code for video : 7
    path('capitalizefirst', views.capfirst, name='capfirst'),   # code for video : 7
    path('newlineremove', views.newlineremove, name='newlineremove'),   # code for video : 7
    path('spaceremove', views.spaceremove, name='spaceremove'),     # code for video : 7
    path('charcount', views.charcount, name='charcount'),       # code for video : 7

    path('templates', views.tem_fun, name='templates'),       # code for video : 8


    path('html9', views.html9_func, name='html9'),    # code for video : 9
    path('removepunc', views.removepunc, name='rempun'),    # code for video : 9


    path('html10', views.html10_func, name='html10'),     # code for video : 10
    path('analyze', views.analyze, name='analyze')    # code for video : 10
]
