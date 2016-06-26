from django.conf.urls import url

from views import ShowClass
from views import LoginClass
from views import CreateClass
from views import DeleteClass
from views import UpdateClass
from views import DashboardClass

from views import logout

app_name = 'client'

urlpatterns = [
    #import pandas, from pandas import *, and  from pandas import DataFrame
    #url(r'^show/(?P<pk>\d+)/$', views.ShowView.as_view(), name = 'show'),
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^dashboard/$', DashboardClass.as_view(), name = 'dashboard'),

    url(r'^show/(?P<username_url>\w+)/$', ShowClass.as_view(), name = 'show'),
    url(r'^edit/$', UpdateClass.as_view(), name = 'edit'),
    
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^delete/(?P<username_url>\w+)/$', DeleteClass.as_view(), name = 'delete'),

    #url(r'^edit/(?P<username_url>\w+)/$', views.Update.as_view(), name = 'edit'),
   ]

