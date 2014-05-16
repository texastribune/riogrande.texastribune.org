from django.contrib import admin
from django.contrib.gis.db import models
from django.forms import widgets

from .models import Ping
from .widgets import LatLonWidget


class PingAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'

    formfield_overrides = {
        models.PointField: {'widget': LatLonWidget}
    }


admin.site.register(Ping, PingAdmin)
