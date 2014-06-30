from django.contrib.gis.db import models

from photos.models import Photo

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsManager

from days.models import Day


class Post(models.Model):

    # publication fields
    pub_date = models.OneToOneField(Day, related_name='post_for')
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    # content fields
    text = models.TextField()
    lede_art = models.ForeignKey(Photo)
    location = models.PointField()

    objects = models.GeoManager()
    published = PublishedObjectsManager()

    def __unicode__(self):
        return self.headline
