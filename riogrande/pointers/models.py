from django.db import models

from photos.models import Photo

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsManager


class Pointer(models.Model):

    # publication fields
    pub_date = models.DateTimeField()
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    url = models.URLField()

    # content fields
    summary = models.TextField()
    lede_art = models.ForeignKey(Photo)

    objects = models.Manager()
    published = PublishedObjectsManager()

    def get_absolute_url(self):
        return self.url
