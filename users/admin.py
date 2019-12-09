from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'types', 'join_year')
    list_filter = ('types', 'join_year')


admin.site.register(UserProfile, UserProfileAdmin)