from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    list_display = 'first_name', 'last_name', 'username', 'id'
    list_display_links = 'first_name', 'username', 'id',
    search_fields = ('id', 'first_name', 'username')
    
    fieldsets = ((None, {'fields': ('username', 'password', 'id', 'bio_details', 'profile_photo')}),
                 (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                 (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'groups',),}),
                 (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                 )
    readonly_fields = ('id', 'last_login', 'date_joined')



