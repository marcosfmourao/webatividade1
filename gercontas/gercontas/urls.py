from django.conf.urls import url

from contas import views

urlpatterns = [

    url(r'^contaid/(?P<pk>[0-9]+)/$', views.contaid, name='pessoaid'),

    url(r'^$', views.index, name='index'),
    url(r'^contas/', views.contas, name='index'),
]