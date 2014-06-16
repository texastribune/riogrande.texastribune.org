from django.db import models

from days.models import Day
from photos.models import Photo

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsManager


class Story(models.Model):

    # publication fields
    pub_date = models.OneToOneField(Day, related_name='story_for')
    pub_status = models.CharField(max_length=1,
                                  choices=PublicationStatus.choices,
                                  default=PublicationStatus.Draft)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=150, default=u'')
    author_email = models.EmailField(max_length=100)

    # content fields
    summary = models.TextField()
    text = models.TextField()
    lede_art = models.ForeignKey(Photo)

    published = PublishedObjectsManager()

    def __unicode__(self):
        return self.headline
