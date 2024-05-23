from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

    empty_value_display = '-отсутствует-'


admin.site.register(Post, PostAdmin)
