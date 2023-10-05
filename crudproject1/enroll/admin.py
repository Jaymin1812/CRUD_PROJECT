from django.contrib import admin

# Register your models here.

from .models import User

@admin.register(User)
class useradmin(admin.ModelAdmin): 
    list_display = ('id','name','email','password')
