from django.conf.urls import url

from .views import CreateClass
from .views import ListClass
from .views import ShowClass
from .views import EditClass


app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
		url(r'^show/(?P<slug>\w+)/$', ShowClass.as_view(), name = 'show'),
		url(r'^edit/(?P<slug>\w+)/$', EditClass.as_view(), name = 'edit'),
    url(r'^my/projects$', ListClass.as_view(), name = 'own'),
   ]
