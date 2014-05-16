# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime


class Measurement(models.Model):

    # publication fields
    pub_date = models.DateTimeField(u'Date/time of measurement')

    # location fields
    location = models.PointField()

    # content fields
    air_temperature = models.FloatField(null=True, blank=True,
                                        help_text=u'in degrees Celsius')
    conductivity = models.FloatField(null=True, blank=True,
                                     help_text=u'in μS/cm')
    depth = models.FloatField(null=True, blank=True,
                              help_text=u'in meters')
    dissolved_oxygen = models.FloatField(null=True, blank=True,
                                         help_text=u'in mg/L')
    e_coli = models.IntegerField(null=True, blank=True,
                                 help_text=u'colonies per 100 ml')
    ph_level = models.FloatField(null=True, blank=True,
                                 validators=[
                                     MaxValueValidator(14.0),
                                     MinValueValidator(0.0),
                                 ],
                                 help_text=u'must be between 0.0 and 14.0')
    secchi_disk_transparency = models.FloatField(null=True, blank=True,
                                                 help_text=u'in meters')
    water_temperature = models.FloatField(null=True, blank=True,
                                          help_text=u'in degrees Celsius')

    def __unicode__(self):
        return localtime(self.pub_date).strftime('%B %d, %Y at %I:%M %p')
