from django.contrib import admin

from . import models


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


admin.site.register(models.Measurement, MeasurementAdmin)
