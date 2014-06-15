from django.contrib import admin

from .models import Day


class DayAdmin(admin.ModelAdmin):
    pass

admin.site.register(Day, DayAdmin)
