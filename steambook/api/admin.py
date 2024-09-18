from django.contrib import admin
from .models import Airticket


class AirticketAdmin(admin.ModelAdmin):
    list_display = ('title',)

    empty_value_display = '-отсутствует-'


admin.site.register(Airticket, AirticketAdmin)
