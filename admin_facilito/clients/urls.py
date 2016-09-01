from django.conf.urls import url

from views import ShowClass
from views import LoginClass
from views import logout
from views import DashboardClass
from views import CreateClass
from views import EditSocialClass

from views import edit_password
from views import edit_client
from views import reset_password
from views import search


app_name = 'client'

urlpatterns = [
    url(r'^show/(?P<username_url>\w+)/$', ShowClass.as_view(), name = 'show'),
    url(r'^login/$', LoginClass.as_view(), name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^dashboard/$', DashboardClass.as_view(), name = 'dashboard'),
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
    url(r'^edit/$', edit_client, name = 'edit'),
    url(r'^edit/password/$', edit_password, name = 'edit_password'),
    url(r'^edit/social/$', EditSocialClass.as_view(), name = 'edit_social'),
    url(r'^search/$', search, name = 'search'),
   ]

handler404 = 'mysite.views.my_custom_page_not_found_view'
