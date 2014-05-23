from django.contrib import admin
from django.contrib.gis.db import models

from .models import Measurement
from pings.widgets import LatLonWidget


class MeasurementAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None, {
            'fields': [
                'pub_date',
                'location',
            ]
        }),
        ('Measurements', {
            'fields': [
                'conductivity',
                'water_temperature',
                'air_temperature',
                'dissolved_oxygen',
                'ph_level',
                'secchi_disk_transparency',
                'depth',
                'e_coli',
            ]
        })
    ]

    formfield_overrides = {
        models.PointField: {'widget': LatLonWidget}
    }


admin.site.register(Measurement, MeasurementAdmin)
