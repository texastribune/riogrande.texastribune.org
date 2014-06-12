from django.db import models

from photos.models import Photo


class Pointer(models.Model):

    # publication fields
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    url = models.URLField()

    # content fields
    summary = models.TextField()
    lede_art = models.ForeignKey(Photo)

    objects = models.Manager()

    def get_absolute_url(self):
        return self.url
