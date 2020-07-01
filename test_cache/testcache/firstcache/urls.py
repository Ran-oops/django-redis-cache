from django.contrib import admin
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^chche1$', views.chche1, name="chche1"),
    url(r'^chche2$', views.chche2, name="chche2"),
    url(r'^chche3$', views.chche3, name="chche3"),
    ]