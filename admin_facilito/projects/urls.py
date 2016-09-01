from django.conf.urls import url

from .views import CreateClass
from .views import ListClass
from .views import ShowClass
from .views import EditClass
from .views import edit
from .views import add_user


app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
		url(r'^show/(?P<slug>[\w-]+)/$', ShowClass.as_view(), name='show'),
    url(r'^my/projects$', ListClass.as_view(), name = 'own'),
    url(r'^edit/(?P<slug>[\w-]+)/$', edit, name = 'edit'),
    url(r'^add/user/$', add_user, name = 'add_user'),
   ]
