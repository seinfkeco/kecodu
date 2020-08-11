# -*- coding: utf-8 -*-
__auther__ = '35942'

from urllib.parse import quote, unquote
from django.contrib import admin
from django.urls import path, include,register_converter
from django.conf.urls import url, include
from keco.api import views as api_views

from keco.dudu import views as dudu_view

urlpatterns = [

    path('api/v1/wfinfo', dudu_view.WfInfoView.as_view(), name='keco-dudu-wfinfo'),

]