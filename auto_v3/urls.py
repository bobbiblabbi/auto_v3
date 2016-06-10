from django.conf.urls import include, url
from django.contrib import admin
from automatization.views import *
from django.shortcuts import render
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^save_ready_template/(?P<id>\d+)/$', save_ready_template, name='save-ready-template'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',  'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    url(r'^$', home_page, name='home-page'),
    url(r'^shablon/(?P<id>\d+)$', template_page, name='template-page'),
    url(r'^delete_user/(?P<id>\d+)/$', delete_user, name='delete-user'),
    url(r'^automatization_page/$', save_template, name='save-template'),
    url(r'^send_email/(?P<id>\d+)/$', send_email, name='send-email'),
    url(r'^home_page/$', home_page, name='home-page'),
    url(r'^file_save/(?P<id>\d+)/$', file_save, name='file-save'),
    url(r'^document/(?P<id>\d+)/$', document, name='document-page'),
    url(r'^create_template_page/(?P<id>\d+)/$', create_template, name='create-template-page'),
    url(r'^get_page_number/$', get_pages, name='get-pages'),
]
