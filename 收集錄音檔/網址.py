# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from 收集錄音檔.介面 import 全部語料
from 收集錄音檔.介面 import 加語料
from 收集錄音檔.介面 import 看語料


urlpatterns = [
    url(r'^$', 全部語料, name='首頁'),
    url(r'^加$', 加語料, name='加'),
    url(r'^改/(?P<pk>\d+)$', 加語料, name='改'),
    url(r'^看/(?P<pk>\d+)$', 看語料, name='看'),
    url(r'^錄音檔/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^', 全部語料),
]
