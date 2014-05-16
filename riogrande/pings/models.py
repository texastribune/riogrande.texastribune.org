from django.contrib.gis.db import models

from django.utils.timezone import localtime


class Ping(models.Model):
    location = models.PointField()
    pub_date = models.DateTimeField()
    api_id = models.PositiveIntegerField(unique=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return '({0}, {1}) on {2}'.format(
            self.location.y,
            self.location.x,
            localtime(self.pub_date).strftime('%B %d, %Y at %I:%M %p'))
