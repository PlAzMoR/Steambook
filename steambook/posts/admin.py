from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('text',)

    empty_value_display = '-отсутствует-'


admin.site.register(Post, PostAdmin)
