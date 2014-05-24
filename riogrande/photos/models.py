from django.db import models

from django.utils.text import slugify
from django.utils.timezone import now

from sortedm2m.fields import SortedManyToManyField


class Photo(models.Model):
    image = models.ImageField(
        max_length=100,
        upload_to='photos/%Y/%m')
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    caption = models.TextField(blank=True)
    date_added = models.DateTimeField(default=now)
    is_public = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)


class Gallery(models.Model):
    date_added = models.DateTimeField(default=now)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)

    photos = SortedManyToManyField(
        Photo,
        related_name='galleries',
        verbose_name='photos',
        null=True,
        blank=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return self.title
