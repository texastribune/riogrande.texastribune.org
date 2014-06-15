# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsManager

from days.models import Day


class Measurement(models.Model):

    # publication fields
    pub_date = models.OneToOneField(
        Day,
        related_name='measurement_for',
        null=True)
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)

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

    objects = models.GeoManager()
    published = PublishedObjectsManager()

    def __unicode__(self):
        return localtime(self.pub_date.date).strftime('%B %d, %Y at %I:%M %p')
