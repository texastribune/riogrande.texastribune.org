from datetime import datetime

from django.contrib.gis.db import models

from django.utils.dateformat import DateFormat

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsGeoManager

from days.models import Day

import pytz


class Ping(models.Model):
    location = models.PointField()
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Published)
    pub_date = models.ForeignKey(
        Day,
        related_name='pings',
        null=True)
    pub_time = models.TimeField()
    api_id = models.PositiveIntegerField(unique=True)

    objects = models.GeoManager()
    published = PublishedObjectsGeoManager()

    def __unicode__(self):
        return '({0}, {1}) on {2}'.format(
            self.location.y,
            self.location.x,
            self.pub_date.date.isoformat())

    @property
    def tz_pub_datetime(self):
        date = datetime.combine(self.pub_date.date, self.pub_time)
        central = pytz.timezone('US/Central')
        date = date.replace(tzinfo=pytz.UTC).astimezone(central)

        return DateFormat(date).format('g:i a')
