from django.contrib.gis.db import models

from django.utils.timezone import localtime

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsGeoManager

from days.models import Day


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
            localtime(self.pub_date.date).strftime('%B %d, %Y'))
