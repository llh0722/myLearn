"""llh_django URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from myfirstapp import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'orm', views.orm),
    url(r'login', views.login),
    url(r'index', views.index),
    # 用户url
    url(r'detail-(?P<nid>\d+).html', views.detail),
    url(r'userDel-(?P<nid>\d+)', views.userDel),
    url(r'userEdit-(?P<nid>\d+)', views.userEdit),
    url(r'user_info', views.user_info),
    # 用户组url
    url(r'user_group', views.user_group),
    url(r'groupEdit-(?P<nid>\d+)', views.groupEdit),
    url(r'groupDel-(?P<nid>\d+)', views.groupDel),

    # Business urls
    url(r'business_info$', views.business_info),
    url(r'host_info$', views.host_info),
]


