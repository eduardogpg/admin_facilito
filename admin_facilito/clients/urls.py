from django.conf.urls import url
from . import views

app_name = 'client'

urlpatterns = [
    url(r'^show/$', views.Show.as_view(), name='show'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^create/$', views.create, name='create'),
]