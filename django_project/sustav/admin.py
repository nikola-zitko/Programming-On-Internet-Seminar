from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.admin import *
# Register your models here.

UserAdmin.list_display += ('role','status',)  # don't forget the commas
UserAdmin.list_filter += ('role','status',)
UserAdmin.fieldsets += (('role', {'fields': ('role',)}),('status', {'fields': ('status',)}),)


class Admin(UserAdmin):
    list_display = ('username','email','role', 'status')

admin.site.register(Korisnici, Admin)

admin.site.register(Predmeti)
admin.site.register(Upisi)

