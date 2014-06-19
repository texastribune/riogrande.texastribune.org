from django.contrib import admin
from django.contrib.gis.db import models

from .models import Ping
from .widgets import LatLonWidget


class PingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': LatLonWidget}
    }


admin.site.register(Ping, PingAdmin)
