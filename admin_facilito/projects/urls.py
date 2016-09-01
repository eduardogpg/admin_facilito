from django.conf.urls import url

from .views import CreateClass
from .views import ListClass
from .views import ShowClass
from .views import EditClass
from .views import edit
from .views import collaboration
from .views import add_collaboration

app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
		url(r'^show/(?P<slug>[\w-]+)/$', ShowClass.as_view(), name='show'),
    url(r'^my/projects$', ListClass.as_view(), name = 'own'),
    url(r'^edit/(?P<slug>[\w-]+)/$', edit, name = 'edit'),
    url(r'^(?P<slug>[\w-]+)/collaboration/$', collaboration, name = 'collaboration'),
    url(r'^(?P<slug>[\w-]+)/collaboration/add/(?P<username>[\w-]+)$', add_collaboration, name = 'add_collaboration'),
   ]
