from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import localtime

from days.models import Day
from photos.models import Photo

from riogrande.choices import PublicationStatus
from riogrande.managers import PublishedObjectsStoryManager


class Story(models.Model):

    # publication fields
    pub_date = models.DateTimeField()
    day_pub_date = models.OneToOneField(
        Day,
        related_name='story_for',
        null=True)
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

    published = PublishedObjectsStoryManager()

    class Meta:
        verbose_name_plural = u'stories'

    def __unicode__(self):
        return self.headline

    def save(self, *args, **kwargs):
        day, _ = Day.objects.get_or_create(date=self.pub_date.date())

        self.day_pub_date = day

        super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if not self.slug:
            # is there something better to return? raise an exception?
            return ''
        pub_date = localtime(self.pub_date)
        return reverse('story_detail', kwargs={
            'year': pub_date.strftime('%Y'),
            'month': pub_date.strftime('%m'),
            'day': pub_date.strftime('%d'),
            'slug': self.slug,
        })

    def get_share_url(self):
        pub_date = localtime(self.pub_date)
        return 'http://riogrande.texastribune.org' + reverse('story_detail', kwargs={
            'year': pub_date.strftime('%Y'),
            'month': pub_date.strftime('%m'),
            'day': pub_date.strftime('%d'),
            'slug': self.slug,
        })
