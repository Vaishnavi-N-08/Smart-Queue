from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Branch, CustomUser, Member
# Register your models here.

class CustomeUserAdmin(UserAdmin):
    list_display = ('username', 'address')
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('address','longitude','latitude')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('address','longitude','latitude')
        })
    )
    
admin.site.register(CustomUser,CustomeUserAdmin)

class BranchAdmin(admin.ModelAdmin):
    model = Branch
    list_display = ('name', 'host', 'current', 'total', 'link')

admin.site.register(Branch, BranchAdmin)


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ('voter_id', 'branch','token')

admin.site.register(Member,MemberAdmin)
