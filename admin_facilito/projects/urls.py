from django.conf.urls import url

from .views import CreateClass
from .views import ListClass


app_name = 'project'

urlpatterns = [
    url(r'^create/$', CreateClass.as_view(), name = 'create'),
    url(r'^my/projects$', ListClass.as_view(), name = 'own'),
    
   ]
