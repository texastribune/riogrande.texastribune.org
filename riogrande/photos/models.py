from django.db import models

from django.utils.text import slugify
from django.utils.timezone import now

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsManager, PublishedObjectsPhotoManager

from sortedm2m.fields import SortedManyToManyField

from days.models import Day


class Photo(models.Model):
    image = models.ImageField(
        max_length=100,
        upload_to='photos/%Y/%m')
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    caption = models.TextField(blank=True)
    credit = models.CharField('photographer', max_length=50, blank=True)
    pub_date = models.DateTimeField(default=now)
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)

    published = PublishedObjectsPhotoManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)


class Gallery(models.Model):
    pub_date = models.OneToOneField(
        Day,
        related_name='gallery_for',
        null=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(blank=True)
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)

    photos = SortedManyToManyField(
        Photo,
        related_name='galleries',
        verbose_name='photos',
        null=True,
        blank=True)

    published = PublishedObjectsManager()

    class Meta:
        ordering = ['-pub_date__date']

    def __unicode__(self):
        return self.title
