from django.contrib import admin

from .models import Client
from .models import SocialNetwork

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class ClientInline(admin.StackedInline):
 model = Client
 can_delete = False
 #fields = ['job',]

class SocialInline(admin.StackedInline):
 model = SocialNetwork
 can_delete = False
 #fields = ['job',]

class UserAdmin(AuthUserAdmin):
 inlines = [ClientInline, SocialInline]

#verbose_name_plurase
class ClientAdmin(admin.ModelAdmin):
	exclude = ('user',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)