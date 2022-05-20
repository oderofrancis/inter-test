from django.contrib import admin
from .models import *

# Register your models here.

class UserNameAdmin(admin.ModelAdmin):
    list_display = ('username','email')

admin.site.register(UserName,UserNameAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('message','created_at','updated_at')

admin.site.register(Message,MessageAdmin)