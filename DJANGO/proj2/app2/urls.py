from django.conf.urls import url
from django.contrib import admin
from app2 import views

urlpatterns = [
    url(r'^$', views.help, name="help")
]
