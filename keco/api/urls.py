"""keco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from urllib.parse import quote, unquote
from django.contrib import admin
from django.urls import path, include,register_converter
from django.conf.urls import url, include
from keco.api import views as api_views
from rest_framework.authtoken import views


# class QuoteConverter:
#     regex = "[\w%~_.-]+"
#
#     def to_python(self, value):
#         return unquote(value)
#
#     def to_url(self, value):
#         return quote(value, safe="")
#
#
# register_converter(QuoteConverter, "quoted")

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    path('api/v1/user/token', api_views.UserTokenView.as_view(), name='keco-api-auth'),
    path('api/v1/users/list', api_views.ListUsers.as_view(), name='keco-api-userslist'), #基于类写
    path('api/v1/users/list1', api_views.users_list, name='keco-api-userslist'), #基于函数
]
